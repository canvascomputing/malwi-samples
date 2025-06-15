# -*- coding: utf-8 -*-
"""articles"""

import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages.api import success as success_message
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext as _
from django.views.generic import View

from colorbox.decorators import popup_redirect

from coop_cms.forms.articles import ArticleLogoForm, ArticleTemplateForm, PublishArticleForm
from coop_cms import models
from coop_cms.generic_views import EditableObjectView
from coop_cms.logger import logger
from coop_cms.settings import (
    get_article_class, get_article_form, get_article_settings_form, get_new_article_form,
    get_articles_category_page_size, homepage_no_redirection
)
from coop_cms.shortcuts import get_article_or_404, get_headlines, redirect_if_alias
from coop_cms.utils import get_model_name, get_model_app, paginate


def get_article_template(article):
    """get article template"""
    template = article.template
    if not template:
        template = 'coop_cms/article.html'
    return template


@login_required
def view_all_articles(request):
    """all article"""

    articles_admin_url = newsletters_admin_url = add_article_url = add_newsletter_url = None

    if request.user.is_staff:
        article_class = get_article_class()

        view_name = 'admin:{0}_{1}_changelist'.format(get_model_app(article_class), get_model_name(article_class))
        articles_admin_url = reverse(view_name)

        newsletters_admin_url = reverse('admin:coop_cms_newsletter_changelist')

        add_newsletter_url = reverse('admin:coop_cms_newsletter_add')

    article_class = get_article_class()
    content_type = ContentType.objects.get_for_model(article_class)
    perm = '{0}.add_{1}'.format(content_type.app_label, content_type.model)
    if request.user.has_perm(perm):
        add_article_url = reverse('coop_cms_new_article')

    return render(
        request,
        'coop_cms/view_all_articles.html',
        {
            'articles': article_class.objects.filter(sites__id=settings.SITE_ID).order_by('-id')[:10],
            'newsletters': models.Newsletter.objects.all().order_by('-id')[:10],
            'editable': True,
            'articles_list_url': articles_admin_url,
            'newsletters_list_url': newsletters_admin_url,
            'add_article_url': add_article_url,
            'add_newsletter_url': add_newsletter_url,
        }
    )


@login_required
def cancel_edit_article(request, url):
    """if cancel_edit, delete the preview image"""
    article = get_article_or_404(slug=url, sites=settings.SITE_ID)
    if article.temp_logo:
        article.temp_logo = ''
        article.save()
    return HttpResponseRedirect(article.get_absolute_url())


@login_required
@popup_redirect
def publish_article(request, url):
    """change the publication status of an article"""
    article = get_article_or_404(slug=url, sites=settings.SITE_ID)

    if not request.user.has_perm('can_publish_article', article):
        raise PermissionDenied

    draft = (article.publication == models.BaseArticle.DRAFT)
    if draft:
        article.publication = models.BaseArticle.PUBLISHED
    else:
        article.publication = models.BaseArticle.DRAFT

    if request.method == "POST":
        form = PublishArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return HttpResponseRedirect(article.get_absolute_url())
    else:
        form = PublishArticleForm(instance=article)

    context_dict = {
        'form': form,
        'article': article,
        'draft': draft,
        'title': _(u"Do you want to publish this article?") if draft else _(u"Make it draft?"),
    }

    return render(
        request,
        'coop_cms/popup_publish_article.html',
        context_dict
    )


@login_required
@popup_redirect
def change_template(request, article_id):
    """change template"""

    article = get_object_or_404(get_article_class(), id=article_id)
    if request.method == "POST":
        form = ArticleTemplateForm(article, request.user, request.POST, request.FILES)
        if form.is_valid():
            article.template = form.cleaned_data['template']
            article.save()
            return HttpResponseRedirect(article.get_edit_url())
    else:
        form = ArticleTemplateForm(article, request.user)

    return render(
        request,
        'coop_cms/popup_change_template.html',
        locals()
    )


@login_required
@popup_redirect
def article_settings(request, article_id):
    """article settings"""
    article = get_object_or_404(get_article_class(), id=article_id)
    article_settings_form_class = get_article_settings_form()

    if not request.user.has_perm('can_edit_article', article):
        raise PermissionDenied

    if request.method == "POST":
        form = article_settings_form_class(request.user, request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            form.save_m2m()
            return HttpResponseRedirect(article.get_absolute_url())
    else:
        form = article_settings_form_class(request.user, instance=article)

    context = {
        'article': article,
        'form': form,
    }
    return render(
        request,
        'coop_cms/popup_article_settings.html',
        context
    )


@login_required
@popup_redirect
def new_article(request):
    """new article"""
    article_class = get_article_class()
    new_article_form = get_new_article_form()

    content_type = ContentType.objects.get_for_model(article_class)
    perm = '{0}.add_{1}'.format(content_type.app_label, content_type.model)

    if not request.user.has_perm(perm):
        raise PermissionDenied

    if request.method == "POST":
        form = new_article_form(request.user, request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            form.save_m2m()
            success_message(request, _(u'The article has been created properly'))
            return HttpResponseRedirect(article.get_edit_url())
    else:
        form = new_article_form(request.user)

    return render(
        request,
        'coop_cms/popup_new_article.html',
        locals()
    )


@login_required
def update_logo(request, article_id):
    """update logo"""
    try:
        article = get_object_or_404(get_article_class(), id=article_id)
        if request.method == "POST":
            form = ArticleLogoForm(request.POST, request.FILES)
            if form.is_valid():
                article.temp_logo = form.cleaned_data['image']
                article.save()
                url = article.logo_thumbnail(True).url
                data = {'ok': True, 'src': url}
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                template = get_template('coop_cms/popup_update_logo.html')
                html = template.render(locals())
                data = {'ok': False, 'html': html}
                return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            form = ArticleLogoForm()

        return render(
            request,
            'coop_cms/popup_update_logo.html',
            locals()
        )
    except Exception:
        logger.exception("update_logo")
        raise


class ArticlesByCategoryView(TemplateView):
    """Show the articles of a given category"""
    category = None

    def get_category(self):
        """return the category"""
        if not self.category:
            slug = self.kwargs['slug']
            self.category = get_object_or_404(models.ArticleCategory, slug=slug, sites__id=settings.SITE_ID)
        return self.category

    def get_articles(self, category):
        """return list of articles for this category, 404 if no articles"""
        articles = category.get_articles_qs().filter(
            publication=models.BaseArticle.PUBLISHED
        ).order_by("-publication_date")

        if articles.count() == 0:
            raise Http404

        return articles

    def get_context_data(self, **kwargs):
        """context"""
        context_data = super(ArticlesByCategoryView, self).get_context_data()
        category = self.get_category()

        if not self.request.user.has_perm('can_view_category', category):
            raise PermissionDenied()

        articles = self.get_articles(category)

        page_obj = paginate(self.request, articles, get_articles_category_page_size(category))

        context_data.update({
            'category': category,
            "articles": list(page_obj),
            'page_obj': page_obj,
        })
        return context_data

    def get_template_names(self):
        """template to use"""
        try:
            category_template = u"coop_cms/categories/{0}.html".format(self.get_category().slug)
            get_template(category_template)
        except TemplateDoesNotExist:
            category_template = "coop_cms/articles_category.html"

        return [category_template]


class ArticleView(EditableObjectView):
    """Article view for edition"""
    model = get_article_class()
    form_class = get_article_form()
    field_lookup = "slug"
    varname = "article"
    as_homepage = False

    def get_object(self):
        """get object"""
        article = get_article_or_404(slug=self.kwargs['slug'], sites=settings.SITE_ID)
        if not self.edit_mode:
            if article.is_homepage and homepage_no_redirection() and not self.as_homepage:
                # Do not authorize access to homepage with its urls in 'homepage_no_redirection' mode
                raise Http404
        return article

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(ArticleView, self).dispatch(request, *args, **kwargs)
        except Http404:
            slug = self.kwargs['slug']
            return redirect_if_alias(slug)

    def can_access_object(self):
        """perms -> 404 if no perms"""

        if self.object.login_required and not self.request.user.is_authenticated():
            raise PermissionDenied

        if self.object.is_archived():
            return super(ArticleView, self).can_view_object()
        return True

    def get_headlines(self):
        """headline"""
        return get_headlines(self.object)

    def get_context_data(self):
        """context"""
        context_data = super(ArticleView, self).get_context_data()
        context_data.update({
            'draft': self.object.publication == models.BaseArticle.DRAFT,
            'headlines': self.get_headlines(),
            'ARTICLE_PUBLISHED': models.BaseArticle.PUBLISHED
        })
        return context_data

    def after_save(self, article):
        """after save"""
        if article.temp_logo:
            article.logo = article.temp_logo
            article.temp_logo = ''
            article.save()

    def get_template(self):
        """get template"""
        return get_article_template(self.object)


class AliasView(View):
    """redirect to another url"""

    def get(self, *args, **kwargs):
        """redirect to aliased page"""
        return redirect_if_alias(path=kwargs.get('path'))

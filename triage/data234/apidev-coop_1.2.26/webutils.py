# -*- coding: utf-8 -*-
"""web utilities"""

import json
from urlparse import urlparse

from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.middleware.csrf import REASON_NO_REFERER, REASON_NO_CSRF_COOKIE
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import get_template
from django.utils.translation import check_for_language, activate, get_language
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from colorbox.decorators import popup_redirect

from coop_cms.logger import logger
from coop_cms.forms.webutils import LanguageSelectionForm
from coop_cms.settings import get_article_class, is_localized
from coop_cms.utils import strip_locale_path, make_locale_path


@csrf_exempt
def hide_accept_cookies_message(request):
    """force cookie warning message to be hidden"""
    if request.method == 'POST':
        request.session['hide_accept_cookie_message'] = True
        data = {"Ok": True}
        return HttpResponse(json.dumps(data), content_type="application/json")
    raise Http404


def _do_change_language(request, lang_code, current_url):
    """change the language and returns redirect URL"""
    if lang_code and check_for_language(lang_code):

        # path is the locale-independent url
        path = strip_locale_path(current_url)[1]

        article_class = get_article_class()
        try:
            # get the translated slug of the current article
            # If switching from French to English and path is /fr/accueil/
            # The next should be : /en/home/

            # Get the article
            next_article = article_class.objects.get(slug=path.strip('/'))

        except article_class.DoesNotExist:
            next_article = None

        if hasattr(request, 'session'):
            request.session['django_language'] = lang_code
        activate(lang_code)

        if next_article:
            next_url = next_article.get_absolute_url()
        else:
            next_url = make_locale_path(path, lang_code)
        return next_url


@csrf_exempt
def change_language(request):
    """change the language"""

    if not is_localized():
        raise Http404

    next_url = request.POST.get('next', None) or request.GET.get('next', None)
    if not next_url:
        url = urlparse(request.META.get('HTTP_REFERER', ''))
        if url:
            next_url = url.path

    if request.method == 'POST':
        lang_code = request.POST.get('language', None)
        after_change_url = request.POST.get('next_url_after_change_lang', None)
        if after_change_url:
            next_url = after_change_url

        go_to_url = _do_change_language(request, lang_code, next_url)
        if go_to_url:
            next_url = go_to_url

    if not next_url:
        next_url = '/'

    return HttpResponseRedirect(next_url)


class DebugErrorCodeView(TemplateView):
    """Debugging: view error page in debug"""

    def get_template_names(self):
        """template to view"""
        return (
            "{0}.html".format(self.kwargs["error_code"]),
        )


def csrf_failure(request, reason=""):
    """
    Custom view used when request fails CSRF protection.

    ENABLED by default by coop_cms unless you set COOP_CMS_DO_NOT_INSTALL_CSRF_FAILURE_VIEW=True in settings.py
    """

    warn_text = u"csrf_failure, reason: {0}".format(reason)
    logger.warn(warn_text)

    template = get_template('coop_cms/csrf_403.html')

    context = {
        'DEBUG': settings.DEBUG,
        'cookie_disabled': reason == REASON_NO_CSRF_COOKIE,
        'no_referer': reason == REASON_NO_REFERER,
    }

    html = template.render(RequestContext(request, context))

    return HttpResponseForbidden(html, content_type='text/html')


@popup_redirect
def switch_language_popup(request):
    """new article"""

    if request.method == "POST":
        form = LanguageSelectionForm(request.POST)
        if form.is_valid():
            lang_code = form.cleaned_data['language']
            url = urlparse(request.META.get('HTTP_REFERER', ''))
            if url:
                prev_url = url.path
            else:
                prev_url = ''
            url = _do_change_language(request, lang_code, prev_url)
            if url:
                return HttpResponseRedirect(url)

    else:
        form = LanguageSelectionForm(initial={'language': get_language()})

    return render(
        request,
        'coop_cms/popup_swicth_language.html',
        {'form': form}
    )

# -*- coding: utf-8 -*-
"""configuration file for coop_bar"""

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse, NoReverseMatch
from django.template.loader import get_template
from django.utils.translation import get_language, ugettext as _

from coop_bar.utils import make_link
from coop_html_editor.settings import get_html_editor

from coop_cms.models import Link, Fragment
from coop_cms.settings import (
    get_article_class, get_navtree_class, cms_no_homepage, hide_media_library_menu, is_localized
)
from coop_cms.utils import get_model_name, get_model_app, get_model_label


def can_do(perm, object_names):
    """can_do decorator: check that user has permission before calling it. If not return empty value"""
    def inner_decorator(func):
        """inner decorator"""
        def wrapper(request, context):
            """wrapper"""
            editable = context.get('editable', None)
            if not editable:
                return
            for object_name in object_names:
                obj = context.get(object_name, None)

                if obj is not None:

                    callback_name = u"coop_cms_{0}_callback".format(perm)
                    callback = context.get(callback_name, None)

                    if callback and request and callback():
                        yes_we_can = func(request, context)
                        if yes_we_can:
                            return yes_we_can
            return
        return wrapper
    return inner_decorator

can_edit_article = can_do('can_edit', ['article'])
can_edit_object = can_do('can_edit', ['article', 'object', 'objects', 'newsletter'])
can_publish_article = can_do('can_publish', ['article'])
can_edit_newsletter = can_do('can_edit', ['newsletter'])
can_edit = can_do('can_edit', ['article', 'newsletter', 'object'])


def can_add_article(func):
    """decorator checking if user can add article"""
    def wrapper(request, context):
        """wrapper"""
        article_class = get_article_class()
        content_type = ContentType.objects.get_for_model(article_class)
        perm = '{0}.add_{1}'.format(content_type.app_label, content_type.model)
        if request and request.user.has_perm(perm):
            return func(request, context)
        return None
    return wrapper


def can_add_link(func):
    """decorator checking if user can add link"""
    def wrapper(request, context):
        """wrapper"""
        content_type = ContentType.objects.get_for_model(Link)
        perm = '{0}.add_{1}'.format(content_type.app_label, content_type.model)
        if request and request.user.has_perm(perm):
            return func(request, context)
        return None
    return wrapper


def django_admin(request, context):
    """show admin"""
    if request and request.user.is_staff:
        return make_link(
            reverse("admin:index"), _(u'Administration'), 'fugue/tables.png',
            classes=['icon', 'alert_on_click']
        )


def django_admin_edit_article(request, context):
    """show edit article in admin"""
    if request and request.user.is_staff and 'article' in context:
        article_class = get_article_class()
        article = context['article']

        view_name = 'admin:{0}_{1}_change'.format(get_model_app(article_class), get_model_name(article_class))
        return make_link(
            reverse(view_name, args=[article.id]), _(u'Article admin'), 'fugue/table.png',
            classes=['icon', 'alert_on_click']
        )


def django_admin_edit_object(request, context):
    """show edit object in admin"""
    if request and request.user.is_staff and context.get('object', None):
        obj = context['object']
        object_class = obj.__class__
        view_name = 'admin:{0}_{1}_change'.format(get_model_app(object_class), get_model_name(object_class))
        try:
            return make_link(
                reverse(view_name, args=[obj.id]),
                _(u'Admin {0}').format(get_model_label(object_class)), 'fugue/table.png',
                classes=['icon', 'alert_on_click']
            )
        except NoReverseMatch:
            pass


def django_admin_add_object(request, context):
    """show add object"""

    if request and request.user.is_staff and (context.get('object', None) or context.get('model', None)):
        object_class = context.get('model', None)
        if not object_class:
            object_class = context['object'].__class__
        view_name = 'admin:{0}_{1}_add'.format(get_model_app(object_class), get_model_name(object_class))
        try:
            return make_link(
                reverse(view_name),
                _(u'Add {0}').format(get_model_label(object_class)), 'fugue/table.png',
                classes=['icon', 'alert_on_click']
            )
        except NoReverseMatch:
            pass


def django_admin_list_objects(request, context):
    """show menu"""
    if request and request.user.is_staff and (context.get('object', None) or context.get('model', None)):
        object_class = context.get('model', None)
        if not object_class:
            object_class = context['object'].__class__
        try:
            view_name = 'admin:{0}_{1}_changelist'.format(get_model_app(object_class), get_model_name(object_class))
            return make_link(
                reverse(view_name),
                _(u'List {0}').format(get_model_label(object_class)), 'fugue/table.png',
                classes=['icon', 'alert_on_click']
            )
        except NoReverseMatch:
            pass


def django_admin_navtree(request, context):
    """show menu"""
    if request and request.user.is_staff:
        coop_cms_navtrees = context.get('coop_cms_navtrees', None)
        if coop_cms_navtrees:
            tree_class = get_navtree_class()
            admin_tree_name = "{0}_{1}".format(get_model_app(tree_class), get_model_name(tree_class))
            if len(coop_cms_navtrees) == 1:
                tree = coop_cms_navtrees[0]
                url = reverse('admin:{0}_change'.format(admin_tree_name), args=[tree.id])
                label = _(u'Navigation tree')
            else:
                url = reverse('admin:{0}_changelist'.format(admin_tree_name))
                label = _(u'Navigation trees')
            return make_link(
                url, label, 'fugue/leaf-plant.png',
                classes=['icon', 'alert_on_click']
            )


def view_all_articles(request, context):
    """show menu"""
    if request and request.user.is_staff:
        return make_link(
            reverse('coop_cms_view_all_articles'), _(u'Articles'), 'fugue/documents-stack.png',
            classes=['icon', 'alert_on_click']
        )


@can_edit_object
def cms_media_library(request, context):
    """show menu"""
    if hide_media_library_menu():
        return
    
    if context.get('edit_mode'):
        return make_link(
            reverse('coop_cms_media_images'), _(u'Media library'), 'fugue/images-stack.png',
            'coopbar_medialibrary', ['icon', 'slide']
        )


@can_edit_object
def cms_upload_image(request, context):
    """show menu"""
    if hide_media_library_menu():
        return
    
    if context.get('edit_mode'):
        return make_link(
            reverse('coop_cms_upload_image'), _(u'Add image'), 'fugue/image--plus.png',
            classes=['coopbar_addfile', 'colorbox-form', 'icon']
        )


@can_edit_article
def cms_update_logo(request, context):
    """show menu"""
    article = context.get('article', None)
    if article and context.get('edit_mode'):
        return make_link(
            reverse('coop_cms_update_logo', args=[article.id]), _(u'Update logo'), 'fugue/image.png',
            classes=['update-logo', 'icon']
        )


@can_edit_object
def cms_upload_doc(request, context):
    """show menu"""
    if hide_media_library_menu():
        return
    
    if context.get('edit_mode'):
        return make_link(
            reverse('coop_cms_upload_doc'), _(u'Add document'), 'fugue/document-import.png',
            classes=['coopbar_addfile', 'colorbox-form', 'icon']
        )


@can_add_article
def cms_new_article(request, context):
    """show menu"""
    if not context.get('edit_mode'):
        url = reverse('coop_cms_new_article')
        return make_link(
            url, _(u'Add article'), 'fugue/document--plus.png',
            classes=['alert_on_click', 'colorbox-form', 'icon']
        )


@can_add_link
def cms_new_link(request, context):
    """show menu"""
    if not context.get('edit_mode'):
        url = reverse('coop_cms_new_link')
        return make_link(
            url, _(u'Add link'), 'fugue/document--plus.png',
            classes=['alert_on_click', 'colorbox-form', 'icon']
        )


@can_add_article
def cms_set_homepage(request, context):
    """show menu"""
    if cms_no_homepage():
        return

    article = context.get('article', None)
    if context.get('edit_mode') and article and (not getattr(article, 'is_homepage', False)):
        url = reverse('coop_cms_set_homepage', args=[article.id])
        return make_link(
            url, _(u'Set homepage'), 'fugue/home--pencil.png',
            classes=['alert_on_click', 'colorbox-form', 'icon']
        )


@can_edit_article    
def cms_article_settings(request, context):
    """show menu"""
    article = context['article']
    url = reverse('coop_cms_article_settings', args=[article.id])
    return make_link(
        url, _(u'Article settings'), 'fugue/gear.png',
        classes=['alert_on_click', 'colorbox-form', 'icon']
    )


@can_edit_object
def cms_save(request, context):
    """show menu"""
    if context.get('edit_mode'):
        #No link, will be managed by catching the js click event
        return make_link(
            '', _(u'Save'), 'fugue/disk-black.png', id="coopbar_save",
            classes=['icon']
        )


@can_edit_object
def cms_cancel(request, context):
    """show menu"""
    if context.get('edit_mode'):
        url = context.get('coop_cms_cancel_url', None)
        if url:
            return make_link(
                url, _(u'Cancel'), 'fugue/cross.png', classes=['alert_on_click', 'icon']
            )


@can_edit_object
def cms_edit(request, context):
    """show menu"""
    if not context.get('edit_mode'):
        url = context.get('coop_cms_edit_url', None)
        if url:
            return make_link(
                url, _(u'Edit'), 'fugue/document--pencil.png', classes=['icon']
            )


@can_publish_article
def cms_publish(request, context):
    """show menu"""
    article = context.get('article')
    if article and ('draft' in context):
        if context['draft']:
            return make_link(
                article.get_publish_url(), _(u'Draft'), 'fugue/lock.png',
                classes=['colorbox-form', 'icon']
            )
        else:
            return make_link(
                article.get_publish_url(), _(u'Published'), 'fugue/globe.png',
                classes=['colorbox-form', 'icon']
            )


def cms_extra_js(request, context):
    """add javascript code"""
    context['html_editor'] = get_html_editor()
    template_ = get_template("coop_cms/_coop_bar_js.html")
    return template_.render(context)


def log_out(request, context):
    """show menu"""
    if request and request.user.is_authenticated() and request.user.is_staff:
        return make_link(
            reverse("logout"), _(u'Log out'), 'fugue/control-power.png', classes=['alert_on_click', 'icon']
        )


@can_add_article
def cms_new_newsletter(request, context):
    """show menu"""
    if not context.get('edit_mode'):
        if getattr(settings, 'COOP_CMS_NEWSLETTER_TEMPLATES', None):
            url = reverse('coop_cms_new_newsletter')
            return make_link(
                url, _(u'Create newsletter'), 'fugue/document--plus.png',
                classes=['alert_on_click', 'colorbox-form', 'icon']
            )


@can_edit_newsletter
def newsletter_admin(request, context):
    """show menu"""
    newsletter = context.get('newsletter')
    object_class = newsletter.__class__
    view_name = 'admin:{0}_{1}_change'.format(get_model_app(object_class), get_model_name(object_class))
    try:
        return make_link(
            reverse(view_name, args=[newsletter.id]),
            _(u'Admin {0}').format(get_model_label(object_class)), 'fugue/table.png',
            classes=['icon', 'alert_on_click']
        )
    except NoReverseMatch:
        pass


@can_edit_newsletter
def newsletter_articles(request, context):
    """show menu"""
    view_name = 'admin:coop_cms_newsletteritem_changelist'
    try:
        return make_link(
            reverse(view_name),
            _(u'Articles ordering'), 'fugue/table.png',
            classes=['icon', 'alert_on_click']
        )
    except NoReverseMatch:
        pass


@can_edit_newsletter
def change_newsletter_settings(request, context):
    """show menu"""
    if not context.get('edit_mode'):
        newsletter = context.get('newsletter')
        url = reverse('coop_cms_newsletter_settings', kwargs={'newsletter_id': newsletter.id})
        return make_link(
            url, _(u'Newsletter settings'), 'fugue/gear.png',
            classes=['icon', 'colorbox-form', 'alert_on_click']
        )


@can_edit_newsletter
def convert_newsletter_to_pdf(request, context):
    """show menu"""
    if 'wkhtmltopdf' in settings.INSTALLED_APPS and not context.get('edit_mode'):
        newsletter = context.get('newsletter')
        url = reverse('coop_cms_newsletter_pdf', args=[newsletter.id, ])
        return make_link(
            url, _(u'Convert to Pdf'), 'fugue/document-pdf.png',
            classes=['icon']
        )


@can_edit_newsletter
def test_newsletter(request, context):
    """show menu"""
    newsletter = context.get('newsletter', None)
    if newsletter:
        url = reverse('coop_cms_test_newsletter', args=[newsletter.id])
        return make_link(
            url, _(u'Send test'), 'fugue/mail-at-sign.png',
            classes=['alert_on_click', 'colorbox-form', 'icon']
        )


@can_edit_object
def cms_add_fragment(request, context):
    """show menu"""
    if request:
        content_type = ContentType.objects.get_for_model(Fragment)
        perm = '{0}.add_{1}'.format(content_type.app_label, content_type.model)
        if request.user.has_perm(perm):
            url = reverse("coop_cms_add_fragment")
            return make_link(
                url, _(u'Add fragment'), 'fugue/block--plus.png',
                classes=['alert_on_click', 'colorbox-form', 'icon', 'if-fragments']
            )


@can_edit_object
def cms_edit_fragments(request, context):
    """show menu"""
    if request:
        content_type = ContentType.objects.get_for_model(Fragment)
        perm = '{0}.change_{1}'.format(content_type.app_label, content_type.model)
        if request.user.has_perm(perm):
            url = reverse("coop_cms_edit_fragments")
            return make_link(
                url, _(u'Edit fragments'), 'fugue/block--pencil.png',
                classes=['alert_on_click', 'colorbox-form', 'icon', 'if-fragments']
            )


def publication_css_classes(request, context):
    """define coop_bar css_class"""
    variable = context.get('article', None) or context.get('object', None)
    if variable:
        if hasattr(variable, 'is_draft') and callable(variable.is_draft) and variable.is_draft():
            return 'is-draft'
        elif hasattr(variable, 'is_archived') and callable(variable.is_archived) and variable.is_archived():
            return 'is-archived'    


def switch_language(request, context):
    if request and request.user.is_staff and is_localized():
        url = reverse('coop_cms_switch_language_popup')
        return make_link(url, _(u'Switch language'), 'fugue/globe-green.png', classes=['colorbox-form', 'icon'])


def load_commands(coop_bar):
    """load commandes"""
    
    menu_list = [
        [
            log_out,
        ],
        [
            django_admin,
            django_admin_edit_article,
            django_admin_edit_object,
            django_admin_navtree,
            view_all_articles,
        ],
        [
            cms_add_fragment,
            cms_edit_fragments,
        ],
        [
            cms_update_logo,
            cms_media_library,
            cms_upload_image,
            cms_upload_doc,
        ],
        [
            cms_new_newsletter,
            change_newsletter_settings,
            newsletter_admin,
            newsletter_articles,
            test_newsletter,
            convert_newsletter_to_pdf,
        ],
        [
            cms_edit,
            cms_save,
            cms_cancel,
        ],
        [
            cms_new_article,
            cms_new_link,
            cms_article_settings,
            cms_set_homepage
        ],
        [
            cms_publish,
        ],
        [
            switch_language,
        ],
    ]

    coop_bar.register(menu_list)
    
    coop_bar.register_css_classes(publication_css_classes)
    
    coop_bar.register_header(cms_extra_js)

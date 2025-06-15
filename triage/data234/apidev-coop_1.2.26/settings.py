# -*- coding: utf-8 -*-
"""
Coop_cms settings : central place for coop_cms settings
the settings should be accessed from here and not directly from django.conf.settings
"""

import os.path
import sys

from django.conf import settings as django_settings
from django.conf.urls import patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from importlib import import_module

from coop_cms.logger import logger


DEFAULT_NAVTREE_CLASS = COOP_CMS_NAVTREE_CLASS = 'coop_cms.NavTree'
DEPRECATED_COOP_CMS_NAVTREE_CLASS = getattr(django_settings, 'COOP_CMS_NAVTREE_CLASS', 'basic_cms.NavTree')
DEFAULT_MEDIA_ROOT = ''


def load_class(settings_key, default_value):
    """returns the form to be used for creating a new article"""
    full_class_name = getattr(django_settings, settings_key, '') or default_value
    if full_class_name:
        try:
            module_name, class_name = full_class_name.rsplit('.', 1)
        except ValueError:
            raise ImportError("Unable to import {0}: full path is required".format(full_class_name))
        module = import_module(module_name)
        class_object = getattr(module, class_name)
        return class_object
    return None


def get_navigable_content_types():
    """returns the list of content types of navigable (which can be used in navigation) models"""
    ct_choices = []
    try:
        content_apps = django_settings.COOP_CMS_CONTENT_APPS
    except AttributeError:
        content_apps = []
        not_to_be_mapped = ('south', 'django_extensions', 'd2rq')
        for module in django_settings.INSTALLED_APPS:
            if (not module.startswith('django.')) and (module not in not_to_be_mapped):
                content_apps.append(module)
    apps_labels = [app.rsplit('.')[-1] for app in content_apps]
    navigable_content_types = ContentType.objects.filter(app_label__in=apps_labels).order_by('app_label')
    for content_type in navigable_content_types:
        is_navnode = ((content_type.model == 'navnode') and (content_type.app_label == 'coop_cms'))
        if (not is_navnode) and 'get_absolute_url' in dir(content_type.model_class()):
            ct_choices.append((content_type.id, content_type.app_label + u'.' + content_type.model))
    return ct_choices


def get_navtree_class(defaut_class=None):
    """
    returns the custom navtree class
    Warning : It is not recommend to define a custom NavTree. This feature is deprecated
    """
    if hasattr(get_navtree_class, '_cache_class'):
        return getattr(get_navtree_class, '_cache_class')
    else:
        navtree_class = None
        if DEFAULT_NAVTREE_CLASS != COOP_CMS_NAVTREE_CLASS:
            full_class_name = COOP_CMS_NAVTREE_CLASS
            app_label, model_name = full_class_name.split('.')
            model_name = model_name.lower()
            try:
                content_type = ContentType.objects.get(app_label=app_label, model=model_name)
                navtree_class = content_type.model_class()
            except Exception:
                navtree_class = None

        if navtree_class is None:
            module = import_module('coop_cms.models')
            navtree_class = module.NavTree
        setattr(get_navtree_class, '_cache_class', navtree_class)
        return navtree_class


def get_article_class():
    """
    returns the custom Article class
    This makes possible to customize the Article model. However, It must inherit from BaseArticle
    """
    if hasattr(get_article_class, '_cache_class'):
        return getattr(get_article_class, '_cache_class')
    else:
        default_value = ""
        if 'coop_cms.apps.basic_cms' in django_settings.INSTALLED_APPS:
            default_value = 'coop_cms.apps.basic_cms.models.Article'

        article_class = load_class('COOP_CMS_ARTICLE_CLASS', default_value)
        if not article_class:
            raise Exception('No article class configured')

        setattr(get_article_class, '_cache_class', article_class)
        return article_class


def get_default_logo():
    """returns the default logo"""
    return getattr(django_settings, 'COOP_CMS_DEFAULT_ARTICLE_LOGO', 'img/default-logo.png')


def get_article_form():
    """returns a form to be used for editing an article"""
    return load_class('COOP_CMS_ARTICLE_FORM', 'coop_cms.forms.ArticleForm')


def get_article_settings_form():
    """returns the form to use for editing article settings"""
    return load_class('COOP_CMS_ARTICLE_SETTINGS_FORM', 'coop_cms.forms.ArticleSettingsForm')


def get_new_article_form():
    """returns the form to be used for creating a new article"""
    return load_class('COOP_CMS_NEW_ARTICLE_FORM', 'coop_cms.forms.NewArticleForm')


def get_newsletter_templates(newsletter, user):
    """returns the list of newsletter templates"""
    try:
        return getattr(django_settings, 'COOP_CMS_NEWSLETTER_TEMPLATES')
    except AttributeError:
        return ()


def get_newsletter_form():
    """returns the form to use for editing a newsletter"""
    return load_class('COOP_CMS_NEWSLETTER_FORM', 'coop_cms.forms.NewsletterForm')


def get_newsletter_settings_form():
    """returns the form to use for for newsletter settings"""
    return load_class('COOP_CMS_NEWSLETTER_SETTINGS_FORM', 'coop_cms.forms.NewsletterSettingsForm')


def get_article_templates(article, user):
    """returns the list of article templates"""
    if hasattr(django_settings, 'COOP_CMS_ARTICLE_TEMPLATES'):
        coop_cms_article_templates = getattr(django_settings, 'COOP_CMS_ARTICLE_TEMPLATES')

        if type(coop_cms_article_templates) in (str, unicode):
            # COOP_CMS_ARTICLE_TEMPLATES is a string :
            #  - a function name that will return a tuple
            #  - a variable name that contains a tuple

            # extract module and function/var names
            module_name, object_name = coop_cms_article_templates.rsplit('.', 1)
            module = import_module(module_name) # import module
            article_templates_object = getattr(module, object_name)  # get the object
            if callable(article_templates_object):
                # function: call it
                article_templates = article_templates_object(article, user)
            else:
                # var: assign
                article_templates = article_templates_object
        else:
            # COOP_CMS_ARTICLE_TEMPLATES is directly a tuple, assign it
            article_templates = coop_cms_article_templates
    else:
        article_templates = None

    return article_templates


def _get_article_setting(article, setting_name, default_value):
    """private function: access an article-dependant setting"""
    try:
        get_setting_name = getattr(django_settings, setting_name)
        try:
            module_name, fct_name = get_setting_name.rsplit('.', 1)
            module = import_module(module_name)
            get_setting = getattr(module, fct_name)
            if callable(get_setting):
                #If the setting is a function get the value as return value of the function call
                value = get_setting(article)
            else:
                #else Take the value as it is
                value = get_setting
        except ValueError:
            value = get_setting_name

    except AttributeError:
        value = default_value
    return value


def get_article_logo_size(article):
    """get the article logo size"""
    return _get_article_setting(article, 'COOP_CMS_ARTICLE_LOGO_SIZE', '48x48')


def get_article_logo_crop(article):
    """get the article logo crop"""
    return _get_article_setting(article, 'COOP_CMS_ARTICLE_LOGO_CROP', 'center')


def get_headline_image_size(article):
    """get the headline image size"""
    return _get_article_setting(article, 'COOP_CMS_HEADLINE_IMAGE_SIZE', '900')


def get_headline_image_crop(article):
    """get the headline image crop"""
    return _get_article_setting(article, 'COOP_CMS_HEADLINE_IMAGE_CROP', None)


def get_max_image_width(image):
    """get the ax image width: avoid user to use very large image"""
    return _get_article_setting(image, 'COOP_CMS_MAX_IMAGE_WIDTH', None)


def get_newsletter_item_classes():
    """get items thant can be used in newsletter"""
    if hasattr(get_newsletter_item_classes, '_cache_class'):
        return getattr(get_newsletter_item_classes, '_cache_class')
    else:
        item_classes = []
        try:
            full_classes_names = getattr(django_settings, 'COOP_CMS_NEWSLETTER_ITEM_CLASSES')
        except AttributeError:
            item_classes = (get_article_class(),)
        else:
            item_classes = []
            for full_class_name in full_classes_names:
                module_name, class_name = full_class_name.rsplit('.', 1)
                module = import_module(module_name)
                item_classes.append(getattr(module, class_name))
            item_classes = tuple(item_classes)

        if not item_classes:
            raise Exception('No newsletter item classes configured')

        setattr(get_newsletter_item_classes, '_cache_class', item_classes)
        return item_classes


def get_newsletter_context_callbacks():
    """get the context for newsletter template"""
    if hasattr(get_newsletter_context_callbacks, '_cache_func'):
        return getattr(get_newsletter_context_callbacks, '_cache_func')
    else:
        try:
            callback_names = getattr(django_settings, 'COOP_CMS_NEWSLETTER_CONTEXT')
        except AttributeError:
            return ()
        else:
            callbacks = []
            for callback_name in callback_names:
                module_name, func_name = callback_name.rsplit('.', 1)
                module = import_module(module_name)
                callbacks.append(getattr(module, func_name))
            callbacks = tuple(callbacks)

        setattr(get_newsletter_context_callbacks, '_cache_func', callbacks)
        return callbacks


def is_localized():
    """return True if site is localized"""
    coop_cms_is_localized = getattr(django_settings, 'COOP_CMS_IS_LOCALIZED', None)
    if coop_cms_is_localized is None:
        if 'modeltranslation' in django_settings.INSTALLED_APPS:
            return True
    return coop_cms_is_localized


def is_multilang():
    """return true if several languages are set"""
    return len(django_settings.LANGUAGES) > 1


def multilang_mode():
    """return true if several languages are set"""
    return len(django_settings.LANGUAGES)


def install_csrf_failure_view():
    """Make possible to customize csrf failure page"""
    dont_do_it = getattr(django_settings, 'COOP_CMS_DO_NOT_INSTALL_CSRF_FAILURE_VIEW', False)
    if not dont_do_it:
        setattr(django_settings, 'CSRF_FAILURE_VIEW', 'coop_cms.views.webutils.csrf_failure')


def cms_no_homepage():
    """returns true if homepage is not managed by coop_cms"""
    return getattr(django_settings, 'COOP_CMS_NO_HOMEPAGE', False)


def hide_media_library_menu():
    """returns True if media is not displayed in coop_bar menu"""
    return getattr(django_settings, 'COOP_CMS_HIDE_MEDIA_LIBRARY_MENU', False)


def is_requestprovider_installed():
    """returns True if possible to get request from anywhere in the code"""
    is_installed = ('coop_cms.utils.RequestMiddleware' in django_settings.MIDDLEWARE_CLASSES)
    if not is_installed:
        logger.warn("You should add coop_cms.utils.RequestMiddleware to the MIDDLEWARE_CLASSES settings")
    return is_installed


def can_rewrite_url():
    """returns True if user is allowed to change article slugs"""
    return getattr(django_settings, 'COOP_CMS_CAN_EDIT_ARTICLE_SLUG', False)


def get_article_views():
    """returns article views"""
    try:
        article_views = getattr(django_settings, 'COOP_CMS_ARTICLE_VIEWS')
        return article_views
    except AttributeError:
        from coop_cms.views.articles import ArticleView
        return {
            'article_view': ArticleView,
            'edit_article_view': ArticleView,
        }


def is_perm_middleware_installed():
    """returns True if permission middleware is installed"""
    return 'coop_cms.middleware.PermissionsMiddleware' in django_settings.MIDDLEWARE_CLASSES


# Check that languages are correctly set
if is_localized():
    if django_settings.LANGUAGE_CODE[:2] != django_settings.LANGUAGES[0][0]:
        text = "coop_cms settings error: LANGUAGE_CODE ({0}) should be first in LANGUAGES (currently first is {1})"
        text = text.format(django_settings.LANGUAGE_CODE[:2], django_settings.LANGUAGES[0][0])
        logger.warning(text)


def is_multi_site():
    """returns True if several sites are configured"""
    return Site.objects.count() > 1


def get_img_folder(instance, filename):
    """image folder"""
    try:
        img_root = django_settings.IMAGE_FOLDER
    except AttributeError:
        img_root = 'img'

    return u'{0}/{1}'.format(img_root, filename)


def get_articles_category_page_size(article_category):
    """returns number of articles for pagination"""
    if article_category.pagination_size:
        return article_category.pagination_size
    return getattr(django_settings, 'COOP_CMS_ARTICLES_CATEGORY_PAGINATION', 10)


def get_url_patterns():
    """return urlspatterns to use"""
    if is_localized():
        return i18n_patterns
    else:
        def url_list(*args):
            if args and isinstance(args[0], (str, unicode, )):
                # remove prefix if any
                return list(args[1:])
            else:
                return list(args)
        return url_list


def get_unit_test_media_root():
    """return unit testing_media root"""
    global DEFAULT_MEDIA_ROOT
    if not DEFAULT_MEDIA_ROOT:
        DEFAULT_MEDIA_ROOT = django_settings.MEDIA_ROOT
        django_settings.MEDIA_ROOT = os.path.join(django_settings.MEDIA_ROOT, '_unit_tests')
    return django_settings.MEDIA_ROOT


def get_media_root():
    """return unit testing_media root if unit test, regular unit test if not"""
    if 'test' in sys.argv:
        return get_unit_test_media_root()
    else:
        return django_settings.MEDIA_ROOT


def homepage_no_redirection():
    """Indicates if the homepage should be served directly or as a redirection (default)"""
    return getattr(django_settings, 'COOP_CMS_HOMEPAGE_NO_REDIRECTION', False)


def get_eastern_languages():
    """returns list of eastern language (not having the english alphabet)"""
    eastern_langs = getattr(django_settings, 'COOP_CMS_EASTERN_LANGUAGES', None)
    if eastern_langs is None:
        eastern_langs = (
            'ru',  # Russian
            'ja',  # Japanese
            'ko',  # Korean
            'iw',  # Hebrew
            'el',  # Greek
            'ar',  # Arabic
            'zh',  # Chinese
            'cn',  # Chinese
        )
    return eastern_langs


def is_cache_enabled():
    """True if cache editable content"""
    return getattr(django_settings, 'COOP_CMS_CACHE', False)

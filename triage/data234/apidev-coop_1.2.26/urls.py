# -*- coding:utf-8 -*-
"""urls"""

from django.conf import settings

from django.conf.urls import include, url

from coop_cms import sitemap
from coop_cms.settings import (
    get_article_views, install_csrf_failure_view
)
from coop_cms.views.newsletters import NewsletterView, NewsletterPdfView
from coop_cms.views import articles, fragments, homepage, links, navigation, newsletters, medialib, webutils
from coop_cms.views.webutils import DebugErrorCodeView

article_views = get_article_views()
article_view = article_views['article_view']
edit_article_view = article_views['edit_article_view']

install_csrf_failure_view()

urlpatterns = [
    url(r'^htm-editor/', include('coop_html_editor.urls')),

    url(r'^cms/change-template/(?P<article_id>\d*)/$', articles.change_template, name="coop_cms_change_template"),
    url(r'^cms/settings/(?P<article_id>\d*)/$', articles.article_settings, name="coop_cms_article_settings"),
    url(r'^cms/new/$', articles.new_article, name="coop_cms_new_article"),
    url(r'^cms/new/article/$', articles.new_article, name="coop_cms_new_article"),
    url(r'^cms/update-logo/(?P<article_id>\d*)/$', articles.update_logo, name="coop_cms_update_logo"),
    url(r'^cms/articles/$', articles.view_all_articles, name="coop_cms_view_all_articles"),
    url(r'^cms/$', articles.view_all_articles),
    url(r'articles/(?P<slug>[-\w]+)/$', articles.ArticlesByCategoryView.as_view(), name="coop_cms_articles_category"),

    url(r'^cms/fragments/add/$', fragments.add_fragment, name='coop_cms_add_fragment'),
    url(r'^cms/fragments/edit/$', fragments.edit_fragments, name='coop_cms_edit_fragments'),

    url(r'^cms/set-homepage/(?P<article_id>\d*)/$', homepage.set_homepage, name='coop_cms_set_homepage'),

    url(r'^cms/new/link/$', links.new_link, name="coop_cms_new_link"),

    url(r'^cms/tree/(?P<tree_id>\d*)/$', navigation.process_nav_edition, name='navigation_tree'),

    url(r'^cms/newsletter/new/$', newsletters.newsletter_settings, name='coop_cms_new_newsletter'),
    url(
        r'^cms/newsletter/settings/(?P<newsletter_id>\d+)/$',
        newsletters.newsletter_settings,
        name='coop_cms_newsletter_settings'
    ),
    url(
        r'^cms/newsletter/(?P<id>\d+)/$',
        NewsletterView.as_view(),
        name='coop_cms_view_newsletter'
    ),
    url(
        r'^cms/newsletter-pdf/(?P<id>\d+)/$',
        NewsletterPdfView.as_view(),
        name='coop_cms_newsletter_pdf'
    ),
    url(
        r'^cms/newsletter/(?P<id>\d+)/cms_edit/$',
        NewsletterView.as_view(edit_mode=True),
        name='coop_cms_edit_newsletter'),

    url(
        r'^cms/newsletter/change-template/(?P<newsletter_id>\d+)/$',
        newsletters.change_newsletter_template,
        name="coop_cms_change_newsletter_template"
    ),
    url(
        r'^cms/newsletter/test/(?P<newsletter_id>\d+)/$',
        newsletters.test_newsletter,
        name="coop_cms_test_newsletter"
    ),
    url(
        r'^cms/newsletter/schedule/(?P<newsletter_id>\d+)/$',
        newsletters.schedule_newsletter_sending,
        name="coop_cms_schedule_newsletter_sending"
    ),

    url(r'^cms/media-images/$', medialib.show_media, {'media_type': 'image'}, name='coop_cms_media_images'),
    url(r'^cms/media-documents/$', medialib.show_media, {'media_type': 'document'}, name='coop_cms_media_documents'),
    url(
        r'^cms/media-photologue/$',
        medialib.show_media,
        {'media_type': 'photologue'},
        name='coop_cms_media_photologue'
    ),
    url(r'^cms/upload-image/$', medialib.upload_image, name="coop_cms_upload_image"),
    url(r'^cms/upload-doc/$', medialib.upload_doc, name="coop_cms_upload_doc"),
    url(r'^cms/private-download/(?P<doc_id>\d*)/$', medialib.download_doc, name='coop_cms_download_doc'),

    url(r'cms/change-language/$', webutils.change_language, name='coop_cms_change_language'),
    url(r'cms/swicth-language/$', webutils.switch_language_popup, name='coop_cms_switch_language_popup'),

    url(
        r'^cms/hide-accept-cookies-message/',
        webutils.hide_accept_cookies_message,
        name='coop_cms_hide_accept_cookies_message'
    ),
]

if settings.DEBUG:
    urlpatterns += [
        url(
            r'^cms/debug-error-code/(?P<error_code>\d{3})/$',
            DebugErrorCodeView.as_view(),
            name='coop_cms_debug_404'
        ),
    ]

if not getattr(settings, "COOP_CMS_DISABLE_DEFAULT_SITEMAP", False):
    urlpatterns += sitemap.urlpatterns

if 'coop_cms.apps.rss_sync' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^rss-sync/', include('coop_cms.apps.rss_sync.urls')),
    ]

if 'coop_cms.apps.test_app' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^this-should-be-only-in-test-mode', include('coop_cms.apps.test_app.urls')),
    ]

# keep these at the end
urlpatterns += [
    url(r'^(?P<url>[-\w]+)/cms_publish/$', articles.publish_article, name='coop_cms_publish_article'),
    url(r'^(?P<url>[-\w]+)/cms_cancel/$', articles.cancel_edit_article, name='coop_cms_cancel_edit_article'),
    url(r'^$', homepage.homepage, name='coop_cms_homepage'),
    url(r'^(?P<slug>[-\w]+)/cms_edit/$', edit_article_view.as_view(edit_mode=True), name='coop_cms_edit_article'),
    url(r'^(?P<slug>[-\w]+)/$', article_view.as_view(), name='coop_cms_view_article'),
    url(r'^(?P<path>.+)$', articles.AliasView.as_view(), name='coop_cms_view_alias'),
    url(r'^coop_bar/', include('coop_bar.urls')),
]

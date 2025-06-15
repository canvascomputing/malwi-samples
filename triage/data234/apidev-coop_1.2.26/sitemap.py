# -*- coding:utf-8 -*-
"""sitemaps"""

from django.conf import settings
from django.conf.urls import url, patterns
from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.utils.translation import activate

from coop_cms.models import BaseArticle, SiteSettings
from coop_cms.settings import get_article_class, is_localized


class LocaleSitemap(Sitemap):
    _current_site = None

    def __init__(self, language=''):
        super(LocaleSitemap, self).__init__()
        self.language = language

    def get_current_site(self):
        """get current site"""
        if not self._current_site:
            self._current_site = Site.objects.get_current()
        return self._current_site

    def get_sitemap_mode(self):
        """define which articles must be included in sitemap"""
        site = self.get_current_site()
        try:
            site_settings = SiteSettings.objects.get(site=site)
            return site_settings.sitemap_mode
        except SiteSettings.DoesNotExist:
            return SiteSettings.SITEMAP_ONLY_SITE

    def location(self, obj):
        if is_localized() and self.language:
            activate(self.language)
        return obj.get_absolute_url()

    def sites(self):
        sitemap_mode = self.get_sitemap_mode()

        if sitemap_mode == SiteSettings.SITEMAP_ALL:
            return Site.objects.all()

        return Site.objects.filter(id=settings.SITE_ID)

    def get_urls(self, page=1, site=None, protocol=None):
        """get urls"""
        urls = []
        for site in self.sites():
            urls.extend(super(LocaleSitemap, self).get_urls(page, site, protocol=protocol))
        return urls


class BaseSitemap(LocaleSitemap):
    """Base class"""
    pass


class ViewSitemap(BaseSitemap):
    """Sitemap base class for django view"""
    view_names = []
    
    def items(self):
        """get items"""

        class item_class(object):
            """a klass wrapper"""
            def __init__(self, view_name):
                self.view_name = view_name
            
            def get_absolute_url(self):
                """get url"""
                return reverse(self.view_name)
            
        return [item_class(view_name) for view_name in self.view_names]


class ArticleSitemap(BaseSitemap):
    """article sitemap"""
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        """items"""
        article_class = get_article_class()
        queryset = article_class.objects.filter(publication=BaseArticle.PUBLISHED)
        items = []
        for site in self.sites():
            items.extend(queryset.filter(sites=site))
        return items

    def lastmod(self, obj):
        """item last modification"""
        return obj.modified


def get_sitemaps(langs=None):
    """return sitemaps"""
    sitemaps = {}
    if is_localized():
        lang_codes = langs or [code[0] for code in settings.LANGUAGES]
        for code in lang_codes:
            site_key = "coop_cms_articles_{0}".format(code)
            sitemaps[site_key] = ArticleSitemap(code)
    else:
        sitemaps['coop_cms_articles'] = ArticleSitemap(None)
    return sitemaps


urlpatterns = patterns('',
    url(
        r'^sitemap\.xml$',
        'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': get_sitemaps()},
        name="coop_cms_sitemap"
    ),
)

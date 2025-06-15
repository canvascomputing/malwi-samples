# -*- coding: utf-8 -*-

from unittest import skipIf

from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.sitemaps.views import sitemap as sitemap_view
from django.core.urlresolvers import reverse
from django.test.client import RequestFactory
from django.utils.translation import activate

from model_mommy import mommy

from coop_cms.models import BaseArticle, SiteSettings
from coop_cms.settings import get_article_class, is_localized, is_multilang
from coop_cms.sitemap import get_sitemaps
from coop_cms.tests import BaseTestCase
from coop_cms.utils import get_url_in_language, slugify


class SitemapTest(BaseTestCase):
    
    def setUp(self):
        self._site2 = mommy.make(Site, id=settings.SITE_ID+1)

    def test_sitemap_empty(self):
        url = reverse("coop_cms_sitemap")
        factory = RequestFactory()
        request = factory.get(url)
        response = sitemap_view(request, get_sitemaps())
        self.assertEqual(200, response.status_code)
    
    def test_sitemap(self):
        site = Site.objects.get_current()
        site2 = self._site2
        
        article_class = get_article_class()
        
        article1 = mommy.make(article_class, slug="test1", publication=BaseArticle.PUBLISHED)
        article2 = mommy.make(article_class, slug="test2", publication=BaseArticle.PUBLISHED)
        article3 = mommy.make(article_class, slug="test3", publication=BaseArticle.PUBLISHED)
        article4 = mommy.make(article_class, slug="test4", publication=BaseArticle.DRAFT)
        
        article2.sites.add(site2)
        article2.save()
        
        article3.sites.remove(site)
        article3.sites.add(site2)
        article3.save()

        factory = RequestFactory()
        request = factory.get('/sitemap.xml')
        response = sitemap_view(request, get_sitemaps())

        self.assertEqual(200, response.status_code)

        self.assertContains(response, site.domain+article1.get_absolute_url())
        self.assertContains(response, site.domain+article2.get_absolute_url())
        self.assertNotContains(response, article3.get_absolute_url())
        self.assertNotContains(response, article4.get_absolute_url())

    def test_sitemap_only_site(self):
        site = Site.objects.get_current()
        site2 = self._site2

        mommy.make(SiteSettings, site=site, sitemap_mode=SiteSettings.SITEMAP_ONLY_SITE)

        article_class = get_article_class()

        article1 = mommy.make(article_class, slug="test1", publication=BaseArticle.PUBLISHED)
        article2 = mommy.make(article_class, slug="test2", publication=BaseArticle.PUBLISHED)
        article3 = mommy.make(article_class, slug="test3", publication=BaseArticle.PUBLISHED)
        article4 = mommy.make(article_class, slug="test4", publication=BaseArticle.DRAFT)

        article2.sites.add(site2)
        article2.save()

        article3.sites.remove(site)
        article3.sites.add(site2)
        article3.save()

        factory = RequestFactory()
        request = factory.get('/sitemap.xml')
        response = sitemap_view(request, get_sitemaps())

        self.assertEqual(200, response.status_code)

        self.assertContains(response, site.domain+article1.get_absolute_url())
        self.assertContains(response, site.domain+article2.get_absolute_url())
        self.assertNotContains(response, article3.get_absolute_url())
        self.assertNotContains(response, article4.get_absolute_url())

    def test_sitemap_all(self):
        site = Site.objects.get_current()
        site2 = self._site2

        site_settings = mommy.make(SiteSettings, site=site, sitemap_mode=SiteSettings.SITEMAP_ALL)

        article_class = get_article_class()

        article1 = mommy.make(article_class, slug="test1", publication=BaseArticle.PUBLISHED)
        article2 = mommy.make(article_class, slug="test2", publication=BaseArticle.PUBLISHED)
        article3 = mommy.make(article_class, slug="test3", publication=BaseArticle.PUBLISHED)
        article4 = mommy.make(article_class, slug="test4", publication=BaseArticle.DRAFT)

        article2.sites.add(site2)
        article2.save()

        article3.sites.remove(site)
        article3.sites.add(site2)
        article3.save()

        factory = RequestFactory()
        request = factory.get('/sitemap.xml')
        response = sitemap_view(request, get_sitemaps())

        self.assertEqual(200, response.status_code)

        self.assertContains(response, site.domain+article1.get_absolute_url())
        self.assertContains(response, site.domain+article2.get_absolute_url())
        self.assertContains(response, site2.domain+article3.get_absolute_url())
        self.assertNotContains(response, article4.get_absolute_url())


class LocaleSitemapTest(SitemapTest):
    """test sitemap can be localized"""

    def setUp(self):
        super(LocaleSitemapTest, self).setUp()
        activate(settings.LANGUAGES[0][0])

    def tearDown(self):
        activate(settings.LANGUAGES[0][0])

    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_sitemap_lang(self):
        site = Site.objects.get_current()
        site2 = self._site2

        article_class = get_article_class()

        article1 = mommy.make(article_class, slug="test1", publication=BaseArticle.PUBLISHED)
        article2 = mommy.make(article_class, slug="test2", publication=BaseArticle.PUBLISHED)
        article3 = mommy.make(article_class, slug="test3", publication=BaseArticle.PUBLISHED)
        article4 = mommy.make(article_class, slug="test4", publication=BaseArticle.DRAFT)

        article2.sites.add(site2)
        article2.save()

        article3.sites.remove(site)
        article3.sites.add(site2)
        article3.save()

        factory = RequestFactory()
        request = factory.get('/sitemap.xml')
        response = sitemap_view(request, get_sitemaps())
        self.assertEqual(200, response.status_code)

        self.assertContains(response, site.domain + article1.get_absolute_url())
        self.assertContains(response, site.domain + article2.get_absolute_url())
        self.assertNotContains(response, article3.get_absolute_url())
        self.assertNotContains(response, article4.get_absolute_url())

        for (lang, name) in settings.LANGUAGES:
            self.assertContains(response, site.domain + get_url_in_language(article1.get_absolute_url(), lang))
            self.assertContains(response, site.domain + get_url_in_language(article2.get_absolute_url(), lang))
            self.assertNotContains(response, get_url_in_language(article3.get_absolute_url(), lang))
            self.assertNotContains(response, get_url_in_language(article4.get_absolute_url(), lang))

    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_sitemap_lang_slug(self):
        """Test that the url is in the locale language"""
        site = Site.objects.get_current()
        from modeltranslation.utils import build_localized_fieldname  # pylint: disable=F0401

        kwargs1 = {}
        kwargs2 = {}

        for lang_code, lang_name in settings.LANGUAGES:
            loc_title_var = build_localized_fieldname('title', lang_code)
            loc_slug_var = build_localized_fieldname('slug', lang_code)
            kwargs1[loc_title_var] = u'article-{0}-1'.format(lang_name)
            kwargs2[loc_title_var] = u'other-article-{0}-2'.format(lang_name)
            kwargs1[loc_slug_var] = slugify(kwargs1[loc_title_var])
            kwargs2[loc_slug_var] = slugify(kwargs2[loc_title_var])

        article_class = get_article_class()

        article1 = mommy.make(article_class, publication=BaseArticle.PUBLISHED, **kwargs1)
        article2 = mommy.make(article_class, publication=BaseArticle.PUBLISHED, **kwargs2)

        factory = RequestFactory()
        request = factory.get('/sitemap.xml')
        response = sitemap_view(request, get_sitemaps())
        self.assertEqual(200, response.status_code)

        for (lang, name) in settings.LANGUAGES:
            activate(lang)
            self.assertContains(response, site.domain + article1.get_absolute_url())
            self.assertContains(response, site.domain + article2.get_absolute_url())

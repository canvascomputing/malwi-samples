# -*- coding: utf-8 -*-

from unittest import skipIf

from django.conf import settings
from django.contrib.sites.models import Site
from django.test.utils import override_settings
from django.utils.translation import get_language

from coop_cms.settings import is_localized, is_multilang, get_article_class
from coop_cms.tests import BaseTestCase
from coop_cms.utils import make_locale_path, slugify


class ArticleSlugTestCase(BaseTestCase):
    """test slug"""
    
    def tearDown(self):
        """after each test"""
        super(ArticleSlugTestCase, self).tearDown()
        site1 = Site.objects.all()[0]
        settings.SITE_ID = site1.id
    
    def test_create_article_same_title(self):
        """test slug with duplicated titles"""
        article_class = get_article_class()
        article1 = article_class.objects.create(title="Titre de l'article")
        for number in xrange(12):
            article2 = article_class.objects.create(title=article1.title)
            self.assertNotEqual(article1.slug, article2.slug)
            self.assertEqual(article1.title, article2.title)
        response = self.client.get(article2.get_absolute_url())
        self.assertEqual(200, response.status_code)
        response = self.client.get(article1.get_absolute_url())
        self.assertEqual(200, response.status_code)
            
    def test_create_article_same_different_sites(self):
        """test slug on different sites"""
        article_class = get_article_class()
        article1 = article_class.objects.create(title="Titre de l'article")
        
        site1 = Site.objects.all()[0]
        site2 = Site.objects.create(domain='hhtp://test2', name="Test2")
        settings.SITE_ID = site2.id
        
        article2 = article_class.objects.create(title=article1.title)
        self.assertNotEqual(article1.slug, article2.slug)
        self.assertEqual(article1.title, article2.title)
        
        response = self.client.get(article1.get_absolute_url())
        self.assertEqual(404, response.status_code)
        
        response = self.client.get(article2.get_absolute_url())
        self.assertEqual(200, response.status_code)
        
        settings.SITE_ID = site1.id
        response = self.client.get(article1.get_absolute_url())
        self.assertEqual(200, response.status_code)
        
    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_create_lang(self):
        """test slug with language"""
        
        article_class = get_article_class()
        article1 = article_class.objects.create(title="Titre de l'article")
        article2 = article_class.objects.create(title=article1.title)
        self.assertNotEqual(article1.slug, article2.slug)
        self.assertEqual(article1.title, article2.title)
        
        trans_lang = settings.LANGUAGES[1][0]
            
        setattr(article1, 'title_'+trans_lang, 'This is the title')
        article1.save()
        
        setattr(article2, 'title_'+trans_lang, getattr(article1, 'title_'+trans_lang))
        article2.save()
        
        article1 = article_class.objects.get(id=article1.id)
        article2 = article_class.objects.get(id=article2.id)
        
        self.assertEqual(getattr(article1, 'title_'+trans_lang), getattr(article2, 'title_'+trans_lang))
        self.assertNotEqual(getattr(article1, 'slug_'+trans_lang), getattr(article2, 'slug_'+trans_lang))
        
    def _get_localized_slug(self, slug):
        """get localized slug"""
        if is_localized():
            return make_locale_path(slug, get_language())
        return slug
    
    def test_create_article_html_in_title(self):
        """create article with html tag in title"""
        article_class = get_article_class()
        article1 = article_class.objects.create(title="<h1>Titre de l'article</h1>")
        response = self.client.get(article1.get_absolute_url())
        self.assertEqual(200, response.status_code)
        
        expected_title = self._get_localized_slug("/titre-de-larticle/")
        self.assertEqual(article1.get_absolute_url(), expected_title)
        
    def test_create_article_complex_html_in_title(self):
        """create article with html tag in title"""
        article_class = get_article_class()
        article1 = article_class.objects.create(title="<p><h2>Titre de <b>l'article</b><h2><div></div></p>")
        response = self.client.get(article1.get_absolute_url())
        self.assertEqual(200, response.status_code)
        expected_title = self._get_localized_slug("/titre-de-larticle/")
        self.assertEqual(article1.get_absolute_url(), expected_title)

    @override_settings(LANGUAGE_CODE='ru', LANGUAGES=(('ru', u'Russian'), ))
    def create_article_non_ascii_char(self):
        """create an article with russian characters"""
        title = u"Миниальбом"
        article_class = get_article_class()
        article1 = article_class.objects.create(title=title)
        response = self.client.get(article1.get_absolute_url())
        self.assertEqual(200, response.status_code)

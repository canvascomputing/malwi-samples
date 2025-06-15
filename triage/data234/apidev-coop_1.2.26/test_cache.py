# -*- coding: utf-8 -*-

from django.conf import settings
from django.test.utils import override_settings

from django.contrib.contenttypes.models import ContentType

from coop_cms.models import BaseArticle
from coop_cms.settings import get_article_class
from coop_cms.tests import BaseArticleTest


@override_settings(
    COOP_CMS_CACHE=True, CACHES={'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}
)
class ArticleTest(BaseArticleTest):
    
    def setUp(self):
        super(ArticleTest, self).setUp()
        self._default_article_templates = settings.COOP_CMS_ARTICLE_TEMPLATES
        settings.COOP_CMS_ARTICLE_TEMPLATES = (
            ('test/newsletter_red.html', 'Red'),
            ('test/newsletter_blue.html', 'Blue'),
        )
        self._HTML_EDITOR_LINK_MODELS = getattr(settings, 'HTML_EDITOR_LINK_MODELS', [])
        article_class = get_article_class()
        content_type = ContentType.objects.get_for_model(article_class)
        settings.HTML_EDITOR_LINK_MODELS = ['{0}.{1}'.format(content_type.app_label, content_type.model)]
        
    def tearDown(self):
        super(ArticleTest, self).tearDown()
        # restore
        settings.COOP_CMS_ARTICLE_TEMPLATES = self._default_article_templates
        settings.HTML_EDITOR_LINK_MODELS = self._HTML_EDITOR_LINK_MODELS

    def test_view_article(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED, content=u"Hello")
        self.assertEqual(article.slug, 'test')
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        self.assertContains(response, u"Hello")

        article.content = u"Bye"
        article.save()
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        self.assertContains(response, u"Hello")

    def test_logged_as_non_staff(self):
        """show page if permission required and authenticated"""
        self._log_as_non_editor()
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED, content=u"Hello")
        self.assertEqual(article.slug, 'test')
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        self.assertContains(response, u"Hello")

        article.content = u"Bye"
        article.save()
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        self.assertContains(response, u"Hello")

    def test_logged_as_staff(self):
        """show page if permission required and authenticated"""
        self._log_as_editor()
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED, content=u"Hello")
        self.assertEqual(article.slug, 'test')
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        self.assertContains(response, u"Hello")

        article.content = u"Bye"
        article.save()
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        self.assertContains(response, u"Bye")

    def _check_article(self, response, data):
        for (key, value) in data.items():
            self.assertContains(response, value)
        
    def test_edit_article(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED)
        
        data = {"title": u'salut', 'content': u'bonjour!'}
        
        self._log_as_editor()
        response = self.client.post(article.get_edit_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_edit_article_invalidate(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED, content=u"Hello")
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        self.assertContains(response, u"Hello")

        data = {"title": u'salut', 'content': u'bonjour!'}
        self._log_as_editor()
        response = self.client.post(article.get_edit_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        self.assertContains(response, data['content'])


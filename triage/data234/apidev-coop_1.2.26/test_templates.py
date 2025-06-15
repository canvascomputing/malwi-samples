# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.urlresolvers import reverse

from model_mommy import mommy

from coop_cms.settings import get_article_class
from coop_cms.tests import BaseArticleTest


class TemplateTest(BaseArticleTest):
    """It should display articles with the right template"""

    def setUp(self):
        super(TemplateTest, self).setUp()
        self._default_article_templates = settings.COOP_CMS_ARTICLE_TEMPLATES
        settings.COOP_CMS_ARTICLE_TEMPLATES = (
            ('coop_cms/article.html', 'coop_cms base article'),
            ('test/article.html', 'test article'),
        )
        
    def tearDown(self):
        super(TemplateTest, self).tearDown()
        # restore
        settings.COOP_CMS_ARTICLE_TEMPLATES = self._default_article_templates

    def test_view_article(self):
        """Check that we are do not using the PrivateArticle anymore"""
        article_class = get_article_class()
        article = mommy.make(article_class, slug="test", publication=article_class.PUBLISHED)
        response = self.client.get(article.get_absolute_url())
        self.assertTemplateUsed(response, 'coop_cms/article.html')
        self.assertEqual(200, response.status_code)
        
    def test_view_article_custom_template(self):
        """Check that we are do not using the PrivateArticle anymore"""
        article_class = get_article_class()
        article = mommy.make(article_class, slug="test", publication=article_class.PUBLISHED, template='test/article.html')
        response = self.client.get(article.get_absolute_url())
        self.assertTemplateUsed(response, 'test/article.html')
        self.assertEqual(200, response.status_code)
        
    def test_change_template(self):
        """Check that we are do not using the PrivateArticle anymore"""
        article_class = get_article_class()
        article = mommy.make(article_class, slug="test")
        self._log_as_editor()
        url = reverse('coop_cms_change_template', args=[article.id])
        response = self.client.post(url, data={'template': 'test/article.html'}, follow=True)
        self.assertEqual(200, response.status_code)
        article = article_class.objects.get(id=article.id)#refresh
        self.assertEqual(article.template, 'test/article.html')
        
    def test_change_template_permission(self):
        """Check that we are do not using the PrivateArticle anymore"""
        article_class = get_article_class()
        article = mommy.make(article_class, slug="test")
        url = reverse('coop_cms_change_template', args=[article.id])
        response = self.client.post(url, data={'template': 'test/article.html'}, follow=True)
        self.assertEqual(200, response.status_code)
        redirect_url = response.redirect_chain[-1][0]
        login_url = reverse('django.contrib.auth.views.login')
        self.assertTrue(redirect_url.find(login_url) >= 0)
        article = article_class.objects.get(id=article.id)  # refresh
        self.assertEqual(article.template, '')



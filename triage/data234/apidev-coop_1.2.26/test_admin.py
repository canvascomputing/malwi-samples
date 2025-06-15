# -*- coding: utf-8 -*-

from django.conf import settings

from django.core.urlresolvers import reverse

from model_mommy import mommy

from coop_cms.models import BaseArticle
from coop_cms.settings import is_localized, get_article_class
from coop_cms.tests import BaseArticleTest, BeautifulSoup
from coop_cms.utils import get_model_app, get_model_name


class ArticleAdminTest(BaseArticleTest):
    
    def setUp(self):
        self.COOP_CMS_CAN_EDIT_ARTICLE_SLUG = getattr(settings, 'COOP_CMS_CAN_EDIT_ARTICLE_SLUG', None)
        
    def tearDown(self):
        setattr(settings, 'COOP_CMS_CAN_EDIT_ARTICLE_SLUG', self.COOP_CMS_CAN_EDIT_ARTICLE_SLUG)
    
    def test_slug_edition_draft(self):
        settings.COOP_CMS_CAN_EDIT_ARTICLE_SLUG = False
        
        self._log_as_staff_editor()
        
        article_class = get_article_class()
        
        article = mommy.make(article_class, slug="test", publication=BaseArticle.DRAFT)

        view_name = 'admin:%s_%s_change' % (get_model_app(article_class), get_model_name(article_class))
        url = reverse(view_name, args=[article.id])
        
        response = self.client.get(url)
        
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)
        
        if is_localized():
            from modeltranslation.utils import build_localized_fieldname
            for (lang, _name) in settings.LANGUAGES:
                field_name = build_localized_fieldname('slug', lang)
                self.assertEqual(soup.select("#id_" + field_name)[0]["type"], "text")
        else:
            self.assertEqual(soup.select("#id_slug")[0]["type"], "text")
                
    def test_slug_edition_published(self):
        settings.COOP_CMS_CAN_EDIT_ARTICLE_SLUG = False
        
        self._log_as_staff_editor()
        
        article_class = get_article_class()
        
        article = mommy.make(article_class, slug="test", publication=BaseArticle.PUBLISHED)
        
        view_name = 'admin:%s_%s_change' % (get_model_app(article_class), get_model_name(article_class))
        url = reverse(view_name, args=[article.id])
        
        response = self.client.get(url)
        
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)
        
        if is_localized():
            from modeltranslation.utils import build_localized_fieldname
            for (lang, _name) in settings.LANGUAGES:
                field_name = build_localized_fieldname('slug', lang)
                self.assertEqual(soup.select("#id_" + field_name)[0]["type"], "hidden")
        else:
            self.assertEqual(soup.select("#id_slug")[0]["type"], "hidden")
                
    def test_slug_edition_published_can_edit(self):
        settings.COOP_CMS_CAN_EDIT_ARTICLE_SLUG = True
        
        self._log_as_staff_editor()
        
        article_class = get_article_class()
        
        article = mommy.make(article_class, slug="test", publication=BaseArticle.PUBLISHED)
        
        view_name = 'admin:%s_%s_change' % (get_model_app(article_class), get_model_name(article_class))
        url = reverse(view_name, args=[article.id])
        
        response = self.client.get(url)
        
        self.assertEqual(200, response.status_code)
        soup = BeautifulSoup(response.content)
        
        if is_localized():
            from modeltranslation.utils import build_localized_fieldname
            for (lang, _name) in settings.LANGUAGES:
                field_name = build_localized_fieldname('slug', lang)
                self.assertEqual(soup.select("#id_" + field_name)[0]["type"], "text")
        else:
            self.assertEqual(soup.select("#id_slug")[0]["type"], "text")

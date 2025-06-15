# -*- coding: utf-8 -*-

from django.test.utils import override_settings

from coop_cms.forms.articles import ArticleSettingsForm, NewArticleForm
from coop_cms.settings import load_class
from coop_cms.tests import BaseTestCase


class LoadClassTest(BaseTestCase):

    @override_settings(COOP_CMS_ARTICLE_SETTINGS_FORM='coop_cms.forms.ArticleSettingsForm')
    def test_load_value(self):
        form_class = load_class('COOP_CMS_ARTICLE_SETTINGS_FORM', 'coop_cms.forms.NewArticleForm')
        self.assertEqual(form_class, ArticleSettingsForm)

    @override_settings(COOP_CMS_ARTICLE_SETTINGS_FORM='')
    def test_load_default(self):
        form_class = load_class('COOP_CMS_ARTICLE_SETTINGS_FORM', 'coop_cms.forms.NewArticleForm')
        self.assertEqual(form_class, NewArticleForm)

    @override_settings(COOP_CMS_ARTICLE_SETTINGS_FORM='')
    def test_load_no_default(self):
        form_class = load_class('COOP_CMS_ARTICLE_SETTINGS_FORM', '')
        self.assertEqual(form_class, None)

    @override_settings(COOP_CMS_ARTICLE_SETTINGS_FORM='')
    def test_load_invalid_value1(self):
        self.assertRaises(ImportError, load_class, 'COOP_CMS_ARTICLE_SETTINGS_FORM', 'blabla')

    @override_settings(COOP_CMS_ARTICLE_SETTINGS_FORM='')
    def test_load_invalid_value2(self):
        self.assertRaises(ImportError, load_class, 'COOP_CMS_ARTICLE_SETTINGS_FORM', 'bla.bla.bla')

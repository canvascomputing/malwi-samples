# -*- coding: utf-8 -*-

from django.conf import settings

from datetime import datetime, timedelta

from django.core.urlresolvers import reverse
from django.template import Template, Context
from django.test.utils import override_settings

from model_mommy import mommy

from coop_cms.models import BaseArticle, ArticleCategory
from coop_cms.settings import get_article_class
from coop_cms.tests import BaseTestCase


@override_settings(COOP_CMS_ARTICLES_CATEGORY_PAGINATION=10)
class ArticlesByCategoryTest(BaseTestCase):
    """Articles category page"""

    def test_view_articles(self):
        """view article by category"""
        article_class = get_article_class()
        cat = mommy.make(ArticleCategory)
        art = mommy.make(article_class, category=cat, title=u"AZERTYUIOP", publication=BaseArticle.PUBLISHED)
        
        url = reverse('coop_cms_articles_category', args=[cat.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, art.title)

    def test_view_articles_ordering(self):
        """view articles by category in order"""
        article_class = get_article_class()
        cat = mommy.make(ArticleCategory)
        
        dt1 = datetime.now() + timedelta(1)
        dt2 = datetime.now()
        dt3 = datetime.now() - timedelta(2)
        dt4 = datetime.now() - timedelta(1)

        art1 = mommy.make(
            article_class, category=cat, title=u"#ITEM1#", publication_date=dt1,
            publication=BaseArticle.PUBLISHED
        )
        art2 = mommy.make(
            article_class, category=cat, title=u"#ITEM2#", publication_date=dt2,
            publication=BaseArticle.PUBLISHED
        )
        art3 = mommy.make(
            article_class, category=cat, title=u"#ITEM3#", publication_date=dt3,
            publication=BaseArticle.PUBLISHED
        )
        art4 = mommy.make(
            article_class, category=cat, title=u"#ITEM4#", publication_date=dt4,
            publication=BaseArticle.PUBLISHED
        )
        
        url = reverse('coop_cms_articles_category', args=[cat.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, art1.title)
        self.assertContains(response, art2.title)
        self.assertContains(response, art3.title)
        self.assertContains(response, art4.title)
        
        content = response.content.decode('utf-8')
        articles = sorted((art1, art2, art3, art4), key=lambda x: x.publication_date)
        articles.reverse()
        
        positions = [content.find(a.title) for a in articles]
        
        self.assertEqual(positions, sorted(positions))

    def test_view_no_articles(self):
        """No article in category: It should return 404"""
        cat = mommy.make(ArticleCategory)
        
        url = reverse('coop_cms_articles_category', args=[cat.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_view_no_published_articles(self):
        """no published article in category: returns 404"""
        article_class = get_article_class()
        cat = mommy.make(ArticleCategory)
        mommy.make(article_class, category=cat, title=u"AZERTYUIOP", publication=BaseArticle.DRAFT)
        
        url = reverse('coop_cms_articles_category', args=[cat.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_view_articles_publication(self):
        """view article by category: publication falg is taken into account"""
        article_class = get_article_class()
        cat = mommy.make(ArticleCategory)
        art1 = mommy.make(article_class, category=cat, title=u"AZERTYUIOP", publication=BaseArticle.PUBLISHED)
        art2 = mommy.make(article_class, category=cat, title=u"QSDFGHJKLM", publication=BaseArticle.DRAFT)
        
        url = reverse('coop_cms_articles_category', args=[cat.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, art1.title)
        self.assertNotContains(response, art2.title)
        
    def test_view_articles_different_categories(self):
        """view article by category : no articles from different category"""
        article_class = get_article_class()
        cat1 = mommy.make(ArticleCategory)
        cat2 = mommy.make(ArticleCategory)
        art1 = mommy.make(article_class, category=cat1, title=u"AZERTYUIOP", publication=BaseArticle.PUBLISHED)
        art2 = mommy.make(article_class, category=cat2, title=u"QSDFGHJKLM", publication=BaseArticle.PUBLISHED)
        
        url = reverse('coop_cms_articles_category', args=[cat1.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, art1.title)
        self.assertNotContains(response, art2.title)
        
    def test_view_articles_unknwonw_categories(self):
        """view article with unknown category: 404"""
        article_class = get_article_class()
        cat = mommy.make(ArticleCategory, name="abcd")
        mommy.make(article_class, category=cat, title=u"AZERTYUIOP", publication=BaseArticle.PUBLISHED)
        
        url = reverse('coop_cms_articles_category', args=["ghjk"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_view_articles_category_template(self):
        """view article with custom template"""
        article_class = get_article_class()
        cat = mommy.make(ArticleCategory, name="Only for unit testing")
        art = mommy.make(article_class, category=cat, title=u"AZERTYUIOP", publication=BaseArticle.PUBLISHED)
        self.assertEqual(cat.slug, "only-for-unit-testing")
        url = reverse('coop_cms_articles_category', args=[cat.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, art.title)
        self.assertContains(response, "This comes from custom template")

    def test_view_articles_category_many(self):
        """view articles by category: check pagination"""

        article_class = get_article_class()
        cat = mommy.make(ArticleCategory)
        for i in range(30):
            mommy.make(
                article_class, category=cat, publication_date=datetime(2014, 3, i+1),
                title=u"AZERTY-{0}-UIOP".format(i), publication=BaseArticle.PUBLISHED
            )
        
        url = reverse('coop_cms_articles_category', args=[cat.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        ids = list(range(30))
        ids.reverse()
        for i in ids[:10]:
            self.assertContains(response, u"AZERTY-{0}-UIOP".format(i))
        for i in ids[10:]:
            self.assertNotContains(response, u"AZERTY-{0}-UIOP".format(i))
            
        response = self.client.get(url+"?page=2")
        self.assertEqual(response.status_code, 200)
        for i in ids[10:20]:
            self.assertContains(response, u"AZERTY-{0}-UIOP".format(i))
        for i in ids[:10]:
            self.assertNotContains(response, u"AZERTY-{0}-UIOP".format(i))

    @override_settings(COOP_CMS_ARTICLES_CATEGORY_PAGINATION=10)
    def test_view_articles_category_pagination_size(self):
        """view articles by category: check pagination"""

        article_class = get_article_class()
        cat = mommy.make(ArticleCategory, pagination_size=5)
        for i in range(30):
            mommy.make(
                article_class, category=cat, publication_date=datetime(2014, 3, i + 1),
                title=u"AZERTY-{0}-UIOP".format(i), publication=BaseArticle.PUBLISHED
            )

        url = reverse('coop_cms_articles_category', args=[cat.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        ids = list(range(30))
        ids.reverse()
        for i in ids[:5]:
            self.assertContains(response, u"AZERTY-{0}-UIOP".format(i))
        for i in ids[5:]:
            self.assertNotContains(response, u"AZERTY-{0}-UIOP".format(i))

        response = self.client.get(url + "?page=2")
        self.assertEqual(response.status_code, 200)
        for i in ids[5:10]:
            self.assertContains(response, u"AZERTY-{0}-UIOP".format(i))
        for i in ids[:5]:
            self.assertNotContains(response, u"AZERTY-{0}-UIOP".format(i))

    @override_settings(COOP_CMS_ARTICLES_CATEGORY_PAGINATION=5)
    def test_view_articles_category_pagination_size_default(self):
        """view articles by category: check pagination"""

        article_class = get_article_class()
        cat = mommy.make(ArticleCategory)
        for i in range(30):
            mommy.make(
                article_class, category=cat, publication_date=datetime(2014, 3, i + 1),
                title=u"AZERTY-{0}-UIOP".format(i), publication=BaseArticle.PUBLISHED
            )

        url = reverse('coop_cms_articles_category', args=[cat.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        ids = list(range(30))
        ids.reverse()
        for i in ids[:5]:
            self.assertContains(response, u"AZERTY-{0}-UIOP".format(i))
        for i in ids[5:]:
            self.assertNotContains(response, u"AZERTY-{0}-UIOP".format(i))

        response = self.client.get(url + "?page=2")
        self.assertEqual(response.status_code, 200)
        for i in ids[5:10]:
            self.assertContains(response, u"AZERTY-{0}-UIOP".format(i))
        for i in ids[:5]:
            self.assertNotContains(response, u"AZERTY-{0}-UIOP".format(i))
        
        
class CoopCategoryTemplateTagTest(BaseTestCase):
    
    def test_use_template(self):
        tpl = Template('{% load coop_utils %}{% coop_category "abc" def %}!!{{def}}!!')
        html = tpl.render(Context({}))
        self.assertEqual(ArticleCategory.objects.count(), 1)
        self.assertEqual(html, "!!abc!!")
        
    def test_use_template_several_times(self):
        tpl = Template(
            '{% load coop_utils %}{% coop_category "joe" bar %}{% coop_category "abc" def %}!!{{def}}-{{bar}}!!'
        )
        html = tpl.render(Context({}))
        self.assertEqual(ArticleCategory.objects.count(), 2)
        self.assertEqual(html, "!!abc-joe!!")
        
    def test_use_template_many_calls(self):
        tpl = Template('{% load coop_utils %}{% coop_category "abc" def %}!!{{def}}!!')
        for i in range(10):
            html = tpl.render(Context({}))
        self.assertEqual(ArticleCategory.objects.count(), 1)
        self.assertEqual(html, "!!abc!!")
    
    def test_use_template_many_calls_not_slug(self):
        tpl = Template('{% load coop_utils %}{% coop_category "Ab CD" def %}!!{{def}}!!')
        html = ""
        for i in range(10):
            html = tpl.render(Context({}))
        self.assertEqual(ArticleCategory.objects.count(), 1)
        self.assertEqual(html, "!!Ab CD!!")
        
    def test_use_template_existing_category(self):
        mommy.make(ArticleCategory, name="abc")
        tpl = Template('{% load coop_utils %}{% coop_category "abc" def %}!!{{def}}!!')
        html = tpl.render(Context({}))
        self.assertEqual(ArticleCategory.objects.count(), 1)
        self.assertEqual(html, "!!abc!!")
        
    def test_use_template_as_variable(self):
        mommy.make(ArticleCategory, name="abc")
        tpl = Template('{% load coop_utils %}{% coop_category cat def %}!!{{def}}!!')
        html = tpl.render(Context({'cat': u"abc"}))
        self.assertEqual(ArticleCategory.objects.count(), 1)
        self.assertEqual(html, "!!abc!!")
        
    def test_view_category_articles(self):
        cat = mommy.make(ArticleCategory, name="abc")
        art1 = mommy.make(
            get_article_class(), slug="test1", category=cat, publication=True, publication_date=datetime.now()
        )
        art2 = mommy.make(
            get_article_class(), slug="test2", category=cat, publication=True,
            publication_date=datetime.now()-timedelta(1)
        )
        
        self.assertEqual(list(cat.get_articles_qs().all()), [art2, art1])

    def test_view_category_articles_not_all_published(self):
        cat = mommy.make(ArticleCategory, name="abc")
        art1 = mommy.make(get_article_class(), slug="test1", category=cat, publication=False)
        art2 = mommy.make(get_article_class(), slug="test2", category=cat, publication=True)

        self.assertEqual(list(cat.get_articles_qs().all()), [art2])

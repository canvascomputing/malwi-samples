# -*- coding: utf-8 -*-

from datetime import timedelta

from django.contrib.sites.models import Site
from django.conf import settings
from django.core.urlresolvers import reverse

from model_mommy import mommy

from coop_cms.models import BaseArticle, ArticleCategory
from coop_cms.settings import get_article_class
from coop_cms.tests import BaseArticleTest, BaseTestCase, BeautifulSoup

        
class MultiSiteTest(BaseTestCase):
    
    def tearDown(self):
        super(MultiSiteTest, self).tearDown()
        site1 = Site.objects.all()[0]
        settings.SITE_ID = site1.id
    
    def test_view_article(self):
        site1 = Site.objects.all()[0]
        site2 = Site.objects.create(domain='hhtp://test2', name="Test2")
        settings.SITE_ID = site1.id
        
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED)
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)

    def test_view_article_on_site2(self):
        site1 = Site.objects.all()[0]
        site2 = Site.objects.create(domain='hhtp://test2', name="Test2")
        settings.SITE_ID = site2.id
        
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED)
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        
    def test_view_article_on_all_sites(self):
        site1 = Site.objects.all()[0]
        site2 = Site.objects.create(domain='hhtp://test2', name="Test2")
        settings.SITE_ID = site1.id
        
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED)
        article.sites.add(site2)
        article.save()
        
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        
        settings.SITE_ID = site2.id
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)

    def test_view_404_site2(self):
        site1 = Site.objects.all()[0]
        site2 = Site.objects.create(domain='hhtp://test2', name="Test2")
        settings.SITE_ID = site1.id
        
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED)
        
        settings.SITE_ID = site2.id
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(404, response.status_code)
        
    def test_view_only_site2(self):
        site1 = Site.objects.all()[0]
        site2 = Site.objects.create(domain='hhtp://test2', name="Test2")
        settings.SITE_ID = site1.id
        
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED)
        article.sites.remove(site1)
        article.sites.add(site2)
        article.save()
        
        settings.SITE_ID = site1.id
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(404, response.status_code)
        
        settings.SITE_ID = site2.id
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)


class MultiSiteCategoryTest(BaseArticleTest):

    def setUp(self):
        self.settings_site_id = settings.SITE_ID
        settings.SITE_ID = 1

    def tearDown(self):
         settings.SITE_ID = self.settings_site_id

    def test_article_category_other_site(self):
        article_class = get_article_class()
        site1 = Site.objects.get(id=settings.SITE_ID)
        site2 = mommy.make(Site)

        cat = mommy.make(ArticleCategory)

        art1 = mommy.make(article_class, slug="test1", category=cat, publication=BaseArticle.PUBLISHED)

        art2 = mommy.make(
            article_class, slug="test2", category=cat, publication=BaseArticle.PUBLISHED,
            publication_date=art1.publication_date+timedelta(1))
        art2.sites.add(site2)
        art2.sites.remove(site1)
        art2.save()

        art3 = mommy.make(article_class, slug="test3", category=cat, publication=BaseArticle.PUBLISHED,
            publication_date=art1.publication_date-timedelta(1))
        art3.sites.add(site2)
        art3.sites.remove(site1)
        art3.save()

        self.assertEqual(art1.previous_in_category(), None)
        self.assertEqual(art1.next_in_category(), None)

    def test_article_category_same_site(self):
        article_class = get_article_class()
        site1 = Site.objects.get(id=settings.SITE_ID)
        site2 = mommy.make(Site)

        cat = mommy.make(ArticleCategory)

        art1 = mommy.make(article_class, slug="test1", category=cat, publication=BaseArticle.PUBLISHED)

        art2 = mommy.make(article_class, slug="test2", category=cat, publication=BaseArticle.PUBLISHED,
            publication_date=art1.publication_date+timedelta(1))

        art3 = mommy.make(article_class, slug="test3", category=cat, publication=BaseArticle.PUBLISHED,
            publication_date=art1.publication_date-timedelta(1))
        art3.sites.add(site2)
        art3.save()

        self.assertEqual(art1.previous_in_category(), art3)
        self.assertEqual(art1.next_in_category(), art2)

    def test_article_category_not_published(self):
        article_class = get_article_class()
        site1 = Site.objects.get(id=settings.SITE_ID)
        site2 = mommy.make(Site)

        cat = mommy.make(ArticleCategory)

        art1 = mommy.make(article_class, slug="test1", category=cat, publication=BaseArticle.PUBLISHED)

        art2 = mommy.make(article_class, slug="test2", category=cat, publication=BaseArticle.DRAFT,
            publication_date=art1.publication_date+timedelta(1))

        art3 = mommy.make(article_class, slug="test3", category=cat, publication=BaseArticle.DRAFT,
            publication_date=art1.publication_date-timedelta(1))
        art3.sites.add(site2)
        art3.save()

        self.assertEqual(art1.previous_in_category(), None)
        self.assertEqual(art1.next_in_category(), None)

    def test_article_category(self):
        self._log_as_editor()

        article_class = get_article_class()
        site1 = Site.objects.get(id=settings.SITE_ID)
        site2 = mommy.make(Site)

        cat = mommy.make(ArticleCategory)
        self.assertEqual(list(cat.sites.all()), [site1])

        cat2 = mommy.make(ArticleCategory)
        cat2.sites.remove(site1)
        cat2.sites.add(site2)
        cat2.save()
        self.assertEqual(list(cat2.sites.all()), [site2])

        cat3 = mommy.make(ArticleCategory)
        cat3.sites.remove(site1)
        cat3.save()
        self.assertEqual(list(cat3.sites.all()), [])

        art1 = mommy.make(article_class, slug="test", category=cat, publication=BaseArticle.PUBLISHED)

        url = reverse('coop_cms_article_settings', args=[art1.id])
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        soup = BeautifulSoup(response.content)
        cat_choices = soup.select("select#id_category option")
        self.assertEqual(2, len(cat_choices))
        self.assertEqual("", cat_choices[0]["value"])
        self.assertEqual(str(cat.id), cat_choices[1]["value"])
        self.assertEqual(cat.name, cat_choices[1].text)

    def test_view_category_articles(self):
        cat = mommy.make(ArticleCategory, name="abc")

        article_class = get_article_class()
        site1 = Site.objects.get(id=settings.SITE_ID)
        site2 = mommy.make(Site)

        cat = mommy.make(ArticleCategory)
        self.assertEqual(list(cat.sites.all()), [site1])
        cat.sites.add(site2)
        cat.save()

        art1 = mommy.make(article_class, category=cat, publication=True, title=u"#THis is crazy")
        art2 = mommy.make(article_class, category=cat, publication=True, title=u"#Call me maybe")

        art2.sites.remove(site1)
        art2.save()

        url = reverse('coop_cms_articles_category', args=[cat.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, art1.title)
        self.assertNotContains(response, art2.title)

    def test_view_category_of_other_site(self):
        cat = mommy.make(ArticleCategory, name="abc")

        article_class = get_article_class()
        site1 = Site.objects.get(id=settings.SITE_ID)
        site2 = mommy.make(Site)

        cat = mommy.make(ArticleCategory)
        self.assertEqual(list(cat.sites.all()), [site1])

        cat2 = mommy.make(ArticleCategory)
        cat2.sites.remove(site1)
        cat2.sites.add(site2)
        cat2.save()

        art1 = mommy.make(article_class, slug="test1", category=cat, publication=True)
        art2 = mommy.make(article_class, slug="test2", category=cat2, publication=True)

        url = reverse('coop_cms_articles_category', args=[cat2.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

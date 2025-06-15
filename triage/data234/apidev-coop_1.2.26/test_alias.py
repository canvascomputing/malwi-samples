# -*- coding: utf-8 -*-

from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from model_mommy import mommy

from coop_cms.models import Alias
from coop_cms.settings import get_article_class
from coop_cms.tests import BaseTestCase


class AliasTest(BaseTestCase):
    
    def test_redirect(self):
        article_class = get_article_class()
        article = article_class.objects.create(slug="test", title="TestAlias", content="TestAlias")
        alias = mommy.make(
            Alias, path='toto', redirect_url=article.get_absolute_url(), sites=Site.objects.all()
        )
        
        response = self.client.get(alias.get_absolute_url())
        self.assertEqual(response.status_code, 301)
        
        response = self.client.get(alias.get_absolute_url(), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, article.title)

    def test_redirect_no_url(self):
        alias = mommy.make(Alias, path='toto', redirect_url='', sites=Site.objects.all())
        response = self.client.get(alias.get_absolute_url())
        self.assertEqual(response.status_code, 404)
        
    def test_redirect_no_alias(self):
        response = self.client.get(reverse('coop_cms_view_article', args=['toto']))
        self.assertEqual(response.status_code, 404)

    def test_redirect_non_slug(self):
        article_class = get_article_class()
        article = article_class.objects.create(slug="test", title="TestAlias", content="TestAlias")
        alias = mommy.make(
            Alias, path='toto.html', redirect_url=article.get_absolute_url(), sites=Site.objects.all()
        )

        response = self.client.get(alias.get_absolute_url())
        self.assertEqual(response.status_code, 301)

        response = self.client.get(alias.get_absolute_url(), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, article.title)

    def test_redirect_no_slash(self):
        article_class = get_article_class()
        article = article_class.objects.create(slug="test", title="TestAlias", content="TestAlias")
        alias = mommy.make(
            Alias, path='toto', redirect_url=article.get_absolute_url(), sites=Site.objects.all()
        )

        url = alias.get_absolute_url()
        self.assertNotEqual(url[-1], "/")

        response = self.client.get(url)
        self.assertEqual(response.status_code, 301)

        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, article.title)

    def test_redirect_no_slash2(self):
        article_class = get_article_class()
        article = article_class.objects.create(slug="test", title="TestAlias", content="TestAlias")
        alias = mommy.make(
            Alias, path='toto', redirect_url=article.get_absolute_url(), sites=Site.objects.all()
        )

        self.assertNotEqual(alias.get_absolute_url()[-1], "/")
        url = alias.get_absolute_url() + "/"

        response = self.client.get(url)
        self.assertEqual(response.status_code, 301)

        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, article.title)

    def test_redirect_slash(self):
        article_class = get_article_class()
        article = article_class.objects.create(slug="test", title="TestAlias", content="TestAlias")
        alias = mommy.make(
            Alias, path='toto/', redirect_url=article.get_absolute_url(), sites=Site.objects.all()
        )

        self.assertNotEqual(alias.get_absolute_url()[-1], "/")
        url = alias.get_absolute_url()

        response = self.client.get(url)
        self.assertEqual(response.status_code, 301)

        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, article.title)

    def test_redirect_slash2(self):
        article_class = get_article_class()
        article = article_class.objects.create(slug="test", title="TestAlias", content="TestAlias")
        alias = mommy.make(
            Alias, path='/fr/en-us/home', redirect_url=article.get_absolute_url(), sites=Site.objects.all()
        )

        self.assertNotEqual(alias.get_absolute_url()[-1], "/")
        url = alias.get_absolute_url()

        response = self.client.get(url)
        self.assertEqual(response.status_code, 301)

        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, article.title)

    def test_redirect_several_slashes(self):
        article_class = get_article_class()
        article = article_class.objects.create(slug="test", title="TestAlias", content="TestAlias")
        alias = mommy.make(
            Alias, path='toto/and/titi/', redirect_url=article.get_absolute_url(), sites=Site.objects.all()
        )

        url = alias.get_absolute_url()

        response = self.client.get(url)
        self.assertEqual(response.status_code, 301)

        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, article.title)

    def test_redirect_unknown(self):
        response = self.client.get('/fr/en-us/home')
        self.assertEqual(response.status_code, 404)

    def test_redirect_unknown_slashes(self):
        response = self.client.get('/fr/en-us/home/')
        self.assertEqual(response.status_code, 404)

    def test_redirect_non_permanent(self):
        article_class = get_article_class()
        article = article_class.objects.create(slug="test", title="TestAlias", content="TestAlias")
        alias = mommy.make(
            Alias, path='toto', redirect_url=article.get_absolute_url(), redirect_code=302, sites=Site.objects.all()
        )

        url = alias.get_absolute_url()
        self.assertNotEqual(url[-1], "/")

        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, article.title)

    def test_redirect_permanent(self):
        article_class = get_article_class()
        article = article_class.objects.create(slug="test", title="TestAlias", content="TestAlias")
        alias = mommy.make(
            Alias, path='toto', redirect_url=article.get_absolute_url(), redirect_code=301, sites=Site.objects.all()
        )

        url = alias.get_absolute_url()
        self.assertNotEqual(url[-1], "/")

        response = self.client.get(url)
        self.assertEqual(response.status_code, 301)

        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, article.title)

    def test_redirect_no_site(self):
        article_class = get_article_class()
        article = article_class.objects.create(slug="test", title="TestAlias", content="TestAlias")
        alias = Alias.objects.create(
            path='toto', redirect_url=article.get_absolute_url(), redirect_code=301
        )

        url = alias.get_absolute_url()

        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_redirect_not_current_site(self):
        article_class = get_article_class()

        site2 = mommy.make(Site)

        article = article_class.objects.create(slug="test", title="TestAlias", content="TestAlias")
        alias = mommy.make(
            Alias, path='toto', redirect_url=article.get_absolute_url(), redirect_code=301, sites=[site2]
        )

        url = alias.get_absolute_url()

        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

# -*- coding: utf-8 -*-

from django.conf import settings

from datetime import datetime

from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse

from model_mommy import mommy

from coop_cms.models import NavNode, BaseArticle, ArticleCategory
from coop_cms.settings import (
    is_localized, get_article_class, get_article_templates, get_navtree_class, is_perm_middleware_installed,
)
from coop_cms.tests import BaseArticleTest, BeautifulSoup, make_dt
from coop_cms.utils import get_login_url


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

    def _check_article(self, response, data):
        for (key, value) in data.items():
            self.assertContains(response, value)
            
    def _check_article_not_changed(self, article, data, initial_data):
        article = get_article_class().objects.get(id=article.id)

        for (key, value) in data.items():
            self.assertNotEquals(getattr(article, key), value)
            
        for (key, value) in initial_data.items():
            self.assertEquals(getattr(article, key), value)

    def test_view_article(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED)
        self.assertEqual(article.slug, 'test')
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)

    def test_view_article_full_slug(self):
        article = get_article_class().objects.create(title="When I am 64", publication=BaseArticle.PUBLISHED)
        self.assertEqual(article.slug, 'when-i-am-64')
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        
    def test_publication_flag_published(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED)
        self.assertEqual(article.is_draft(), False)
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        
    def test_publication_flag_archived(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.ARCHIVED)
        self.assertEqual(article.is_draft(), False)
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(404, response.status_code)
        
    def test_publication_flag_draft(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.DRAFT)
        self.assertEqual(article.is_draft(), True)
        url = article.get_absolute_url()
        response = self.client.get(url)
        if is_perm_middleware_installed():
            self.assertEqual(302, response.status_code)
            auth_url = get_login_url()
            self.assertRedirects(response, auth_url+'?next='+url)
        else:
            self.assertEqual(403, response.status_code)

    def test_login_required_authenticated(self):
        """show page if permission required and authenticated"""
        self._log_as_non_editor()
        article = get_article_class().objects.create(
            title="test", publication=BaseArticle.PUBLISHED, login_required=True
        )
        url = article.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_login_required_not_authenticated(self):
        """raise permission denied if permission required not authenticated"""
        self.client.logout()
        article = get_article_class().objects.create(
            title="test", publication=BaseArticle.PUBLISHED, login_required=True
        )
        url = article.get_absolute_url()
        response = self.client.get(url)
        if is_perm_middleware_installed():
            self.assertEqual(302, response.status_code)
            auth_url = get_login_url()
            self.assertRedirects(response, auth_url+'?next='+url)
        else:
            self.assertEqual(403, response.status_code)
        
    def test_404_ok(self):
        response = self.client.get("/jhjhjkahekhj", follow=True)
        self.assertEqual(404, response.status_code)
        
    def test_is_navigable(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED)
        if is_localized():
            lang = settings.LANGUAGES[0][0]
            self.assertEqual('/{0}/test/'.format(lang), article.get_absolute_url())
        else:
            self.assertEqual('/test/', article.get_absolute_url())

    def test_create_slug(self):
        article = get_article_class().objects.create(title=u"voici l'été", publication=BaseArticle.PUBLISHED)
        self.assertEqual(article.slug, 'voici-lete')
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        
    def test_edit_article(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED)
        
        data = {"title": 'salut', 'content': 'bonjour!'}
        
        self._log_as_editor()
        response = self.client.post(article.get_edit_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self._check_article(response, data)
        
        data = {"title": 'bye', 'content': 'au revoir'}
        response = self.client.post(article.get_edit_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self._check_article(response, data)

    def test_edit_article_html(self):
        """It should save article correctly"""
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED)

        data = {"title": 'salut', 'content': '<h2>Hello</h2><p>Hello</p>'}

        self._log_as_editor()
        response = self.client.post(article.get_edit_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self._check_article(response, data)

    def test_edit_article_html_with_br(self):
        """It should save article correctly"""
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED)

        data = {"title": 'salut', 'content': '<h2>Hello</h2><p>Hello<br>Cool<br /></p>'}

        self._log_as_editor()
        response = self.client.post(article.get_edit_url(), data=data, follow=True)

        self.assertEqual(response.status_code, 200)
        expected_content = '<h2>Hello</h2><p>Hello<br />Cool<br /></p>'
        data['content'] = expected_content
        self._check_article(response, data)

    def test_edit_article_html_with_img_wrapper(self):
        """It should save article correctly"""
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED)

        content = """
            <p><div
            contenteditable="false"
            style="overflow: hidden; position: relative; display: inline-block; float: none;"
            class="ui-wrapper aloha-image-box-active Aloha_Image_Resize aloha"
            >
                <img src="moby-dick.jpg" style="height: 207px; width: 269px;" class="ui-resizable" />
                <div class="ui-resizable-handle ui-resizable-ne" style="z-index: 1000;"></div>
                <div class="ui-resizable-handle ui-resizable-se ui-icon" style="z-index: 1000;"></div>
                <div class="ui-resizable-handle ui-resizable-sw" style="z-index: 1000;"></div>
                <div class="ui-resizable-handle ui-resizable-nw" style="z-index: 1000;"></div>
            </div></p>
        """

        data = {"title": 'salut', 'content': content}

        self._log_as_editor()
        response = self.client.post(article.get_edit_url(), data=data, follow=True)

        self.assertEqual(response.status_code, 200)

        expected_content = '<p><img class="" src="moby-dick.jpg" style="height: 207px; width: 269px;"/></p>'
        data['content'] = expected_content
        self._check_article(response, data)

    def test_edit_article_draft(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.DRAFT)
        
        data = {"title": 'salut', 'content': 'bonjour!'}
        
        self._log_as_editor()
        response = self.client.post(article.get_edit_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self._check_article(response, data)
        
        data = {"title": 'bye', 'content': 'au revoir'}
        response = self.client.post(article.get_edit_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self._check_article(response, data)
        
    def test_edit_article_archived(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.ARCHIVED)
        
        data = {"title": 'salut', 'content': 'bonjour!'}
        
        self._log_as_editor()
        response = self.client.post(article.get_edit_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self._check_article(response, data)
        
        data = {"title": 'bye', 'content': 'au revoir'}
        response = self.client.post(article.get_edit_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self._check_article(response, data)
        
    def test_post_on_view_article(self):
        initial_data = {'title': "test", 'content': "this is my article content"}
        article = get_article_class().objects.create(publication=BaseArticle.PUBLISHED, **initial_data)
        
        data = {"title": 'salut', 'content': 'bonjour!'}
        
        self._log_as_editor()
        response = self.client.post(article.get_absolute_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 404)
        
        article = get_article_class().objects.get(id=article.id)
        self.assertEquals(article.title, initial_data['title'])
        self.assertEquals(article.content, initial_data['content'])
        
    def test_article_edition_permission(self):
        initial_data = {'title': "test", 'content': "this is my article content"}
        article = get_article_class().objects.create(publication=BaseArticle.PUBLISHED, **initial_data)
        url = article.get_edit_url()
        data = {"title": 'salut', "content": 'oups'}
        response = self.client.post(url, data=data)
        if is_perm_middleware_installed():
            self.assertEqual(302, response.status_code)
            auth_url = get_login_url()
            self.assertRedirects(response, auth_url+'?next='+url)
        else:
            self.assertEqual(403, response.status_code)
        
        article = get_article_class().objects.get(id=article.id)
        self.assertEquals(article.title, initial_data['title'])
        self.assertEquals(article.content, initial_data['content'])
        
    def _is_inline_html_editor_found(self, response):
        self.assertEqual(200, response.status_code)
        inline_editor_init_url = reverse('html_editor_init')
        content = unicode(response.content, 'utf-8')
        return content.find(inline_editor_init_url) > 0
        
    def test_edit_permission(self):
        initial_data = {'title': "ceci est un test", 'content': "this is my article content"}
        article = get_article_class().objects.create(publication=BaseArticle.PUBLISHED, **initial_data)
        response = self.client.get(article.get_absolute_url(), follow=True)
        self.assertEqual(200, response.status_code)
        
        url = article.get_edit_url()
        response = self.client.get(url, follow=False)
        if is_perm_middleware_installed():
            self.assertEqual(302, response.status_code)
            auth_url = get_login_url()
            self.assertRedirects(response, auth_url+'?next='+url)
        else:
            self.assertEqual(403, response.status_code)
    
        self._log_as_editor()
        response = self.client.get(article.get_edit_url(), follow=False)
        self.assertEqual(200, response.status_code)
        
    def test_inline_html_editor_loaded(self):
        initial_data = {'title': u"ceci est un test", 'content': u"this is my article content"}
        article = get_article_class().objects.create(publication=BaseArticle.PUBLISHED, **initial_data)
        response = self.client.get(article.get_absolute_url())
        self.assertFalse(self._is_inline_html_editor_found(response))
        
        self._log_as_editor()
        response = self.client.get(article.get_edit_url())
        self.assertTrue(self._is_inline_html_editor_found(response))
        
    def test_inline_html_editor_links(self):
        slugs = ("un", "deux", "trois", "quatre")
        for slug in slugs:
            get_article_class().objects.create(publication=BaseArticle.PUBLISHED, title=slug)
        initial_data = {'title': "test", 'content': "this is my article content"}
        get_article_class().objects.create(**initial_data)
        
        self._log_as_editor()
        response = self.client.get(reverse('html_editor_init'))
        
        context_slugs = [article.slug for article in response.context['links']]
        for slug in slugs:
            self.assertTrue(slug in context_slugs)
        
    def test_view_draft_article(self):
        self.client.logout()
        article = get_article_class().objects.create(title="test", publication=BaseArticle.DRAFT)
        url = article.get_absolute_url()
        response = self.client.get(url)
        if is_perm_middleware_installed():
            self.assertEqual(302, response.status_code)
            auth_url = get_login_url()
            self.assertRedirects(response, auth_url+'?next='+url)
        else:
            self.assertEqual(403, response.status_code)
        
        self._log_as_editor()
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(200, response.status_code)
        
    def test_accept_regular_html(self):
        article = get_article_class().objects.create(title="test", publication=BaseArticle.PUBLISHED)
        html = '<h1>paul</h1><a href="/" target="_blank">georges</a><p><b>ringo</b></p>'
        html += '<h6>john</h6><img src="/img.jpg"><br><table><tr><th>A</th><td>B</td></tr>'
        data = {'content': html, 'title': 'ok'}
        
        self._log_as_editor()
        response = self.client.post(article.get_edit_url(), data=data, follow=False)
        self.assertEqual(response.status_code, 302)
        
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        
        # checking html content would not work. Check that the article is updated
        for b in ['paul', 'georges', 'ringo', 'john']:
            self.assertContains(response, b)

    def test_publish_article(self):
        initial_data = {'title': "test", 'content': "this is my article content"}
        article = get_article_class().objects.create(publication=BaseArticle.DRAFT, **initial_data)
        
        self._log_as_editor()
        
        data = {
            'publication': BaseArticle.PUBLISHED,
        }
        
        response = self.client.post(article.get_publish_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        article = get_article_class().objects.get(id=article.id)
        self.assertEqual(article.title, initial_data['title'])
        self.assertEqual(article.content, initial_data['content'])
        self.assertEqual(article.publication, BaseArticle.PUBLISHED)

    def test_draft_article(self):
        initial_data = {'title': "test", 'content': "this is my article content"}
        article = get_article_class().objects.create(publication=BaseArticle.PUBLISHED, **initial_data)
        
        self._log_as_editor()
        
        data = {
            'publication': BaseArticle.DRAFT,
        }
        
        response = self.client.post(article.get_publish_url(), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        article = get_article_class().objects.get(id=article.id)
        self.assertEqual(article.title, initial_data['title'])
        self.assertEqual(article.content, initial_data['content'])
        self.assertEqual(article.publication, BaseArticle.DRAFT)
        
    def test_new_article(self):
        article_class = get_article_class()
        
        self._log_as_editor()
        data = {
            'title': "Un titre",
            'publication': BaseArticle.DRAFT,
            'template': get_article_templates(None, self.user)[0][0],
            'navigation_parent': None,
            'sites': [settings.SITE_ID]
        }
        
        response = self.client.post(reverse('coop_cms_new_article'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(article_class.objects.count(), 1)
        article = article_class.objects.all()[0]
        
        self.assertEqual(article.title, data['title'])
        self.assertEqual(article.publication, data['publication'])
        self.assertEqual(article.template, data['template'])
        self.assertEqual(article.navigation_parent, None)
        self.assertEqual(NavNode.objects.count(), 0)
        self.assertEqual([a.id for a in article.sites.order_by("id")], data['sites'])

    def test_view_new_article(self):
        other_site = mommy.make(Site)

        category1 = mommy.make(ArticleCategory)
        category1.sites.clear()
        category1.sites.add(Site.objects.get_current())
        category1.save()

        category2 = mommy.make(ArticleCategory)
        category2.sites.clear()
        category2.sites.add(Site.objects.get_current())
        category2.sites.add(other_site)
        category2.save()

        category3 = mommy.make(ArticleCategory)
        category3.sites.clear()
        category3.sites.add(other_site)
        category3.save()

        category4 = mommy.make(ArticleCategory)
        category4.sites.clear()
        category4.save()

        self._log_as_editor()

        response = self.client.get(reverse('coop_cms_new_article'))
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content)

        categories_select_node = soup.select("select#id_category")[0]

        categories = [node.text for node in categories_select_node.select('option')]

        self.assertEqual(3, len(categories))
        self.assertTrue('---------' in categories)
        self.assertTrue(category1.name in categories)
        self.assertTrue(category2.name in categories)
        self.assertTrue(category3.name not in categories)
        self.assertTrue(category4.name not in categories)

    def test_new_article_two_sites(self):
        other_site = mommy.make(Site)
        article_class = get_article_class()

        self._log_as_editor()
        data = {
            'title': "Un titre",
            'publication': BaseArticle.DRAFT,
            'template': get_article_templates(None, self.user)[0][0],
            'navigation_parent': None,
            'sites': sorted([settings.SITE_ID, other_site.id])
        }

        response = self.client.post(reverse('coop_cms_new_article'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(article_class.objects.count(), 1)
        article = article_class.objects.all()[0]

        self.assertEqual(article.title, data['title'])
        self.assertEqual(article.publication, data['publication'])
        self.assertEqual(article.template, data['template'])
        self.assertEqual(article.navigation_parent, None)
        self.assertEqual(NavNode.objects.count(), 0)
        self.assertEqual([_article.id for _article in article.sites.order_by("id")], data['sites'])

    def test_new_article_without_site(self):
        article_class = get_article_class()

        self._log_as_editor()
        data = {
            'title': "Un titre",
            'publication': BaseArticle.DRAFT,
            'template': get_article_templates(None, self.user)[0][0],
            'navigation_parent': None,
            'sites': []
        }

        response = self.client.post(reverse('coop_cms_new_article'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(article_class.objects.count(), 0)

        soup = BeautifulSoup(response.content)
        self.assertEqual(len(soup.select("ul.errorlist")), 1)

    def test_new_article_invalid_site(self):
        article_class = get_article_class()

        self._log_as_editor()
        data = {
            'title': "Un titre",
            'publication': BaseArticle.DRAFT,
            'template': get_article_templates(None, self.user)[0][0],
            'navigation_parent': None,
            'sites': [settings.SITE_ID, 999]
        }

        response = self.client.post(reverse('coop_cms_new_article'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(article_class.objects.count(), 0)

        soup = BeautifulSoup(response.content)
        self.assertEqual(len(soup.select("ul.errorlist")), 1)

    def test_new_article_invalid_category_site(self):
        article_class = get_article_class()

        category1 = mommy.make(ArticleCategory)
        category1.sites.clear()
        category1.sites.add(Site.objects.get_current())
        category1.save()

        category2 = mommy.make(ArticleCategory)
        category2.sites.clear()
        category2.save()

        self._log_as_editor()
        data = {
            'title': "Un titre",
            'category': category2.id,
            'publication': BaseArticle.DRAFT,
            'template': get_article_templates(None, self.user)[0][0],
            'navigation_parent': None,
            'sites': [settings.SITE_ID]
        }

        response = self.client.post(reverse('coop_cms_new_article'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(article_class.objects.count(), 0)

        soup = BeautifulSoup(response.content)
        self.assertEqual(len(soup.select("ul.errorlist")), 1)

    def test_new_article_title_required(self):
        article_class = get_article_class()

        self._log_as_editor()
        data = {
            'title': "",
            'publication': BaseArticle.DRAFT,
            'template': get_article_templates(None, self.user)[0][0],
            'navigation_parent': None,
            'sites': [settings.SITE_ID]
        }
        
        response = self.client.post(reverse('coop_cms_new_article'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content)
        
        self.assertEqual(article_class.objects.count(), 0)
        self.assertEqual(len(soup.select("ul.errorlist")), 1)
        
    def test_new_article_published(self):
        article_class = get_article_class()
        
        self._log_as_editor()
        data = {
            'title': "Un titre",
            'publication': BaseArticle.PUBLISHED,
            'template': get_article_templates(None, self.user)[0][0],
            'navigation_parent': None,
            'sites': [settings.SITE_ID]
        }
        
        response = self.client.post(reverse('coop_cms_new_article'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(article_class.objects.count(), 1)
        article = article_class.objects.all()[0]
        
        self.assertEqual(article.title, data['title'])
        self.assertEqual(article.publication, data['publication'])
        self.assertEqual(article.template, data['template'])
        self.assertEqual(article.navigation_parent, None)
        self.assertEqual(NavNode.objects.count(), 0)
        
    def test_new_article_anonymous(self):
        article_class = get_article_class()
        
        self._log_as_editor() #create self.user
        self.client.logout()
        data = {
            'title': "Ceci est un titre",
            'publication': BaseArticle.DRAFT,
            'template': get_article_templates(None, self.user)[0][0],
            'navigation_parent': None,
            'sites': [settings.SITE_ID]
        }
        
        response = self.client.post(reverse('coop_cms_new_article'), data=data, follow=True)
        self.assertEqual(200, response.status_code) #if can_edit returns 404 error
        next_url = response.redirect_chain[-1][0]
        login_url = reverse('django.contrib.auth.views.login')
        self.assertTrue(login_url in next_url)
        
        self.assertEqual(article_class.objects.filter(title=data['title']).count(), 0)
        
    def test_new_article_no_perm(self):
        article_class = get_article_class()
        
        self._log_as_editor_no_add()
        data = {
            'title': "Ceci est un titre",
            'publication': BaseArticle.DRAFT,
            'template': get_article_templates(None, self.user)[0][0],
            'navigation_parent': None,
            'sites': [settings.SITE_ID]
        }
        
        response = self.client.post(reverse('coop_cms_new_article'), data=data, follow=True)
        self.assertEqual(403, response.status_code)
        self.assertEqual(article_class.objects.filter(title=data['title']).count(), 0)
        
    def test_new_article_navigation(self):
        article_class = get_article_class()
        
        tree = get_navtree_class().objects.create()
        
        self._log_as_editor()
        data = {
            'title': "Un titre",
            'publication': BaseArticle.PUBLISHED,
            'template': get_article_templates(None, self.user)[0][0],
            'navigation_parent': -tree.id,
            'sites': [settings.SITE_ID]
        }
        
        response = self.client.post(reverse('coop_cms_new_article'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(article_class.objects.count(), 1)
        article = article_class.objects.all()[0]
        
        self.assertEqual(article.title, data['title'])
        self.assertEqual(article.publication, data['publication'])
        self.assertEqual(article.template, data['template'])
        self.assertEqual(article.navigation_parent, -tree.id)
        
        self.assertEqual(NavNode.objects.count(), 1)
        node = NavNode.objects.all()[0]
        self.assertEqual(node.content_object, article)
        self.assertEqual(node.parent, None)
        self.assertEqual(node.tree, tree)
        
    def test_new_article_navigation_leaf(self):
        initial_data = {'title': "test", 'content': "this is my article content"}
        article_class = get_article_class()
        art1 = article_class.objects.create(publication=BaseArticle.PUBLISHED, **initial_data)
        
        tree = get_navtree_class().objects.create()
        ct = ContentType.objects.get_for_model(article_class)
        node1 = NavNode.objects.create(content_type=ct, object_id=art1.id, tree=tree, parent=None)
        
        self._log_as_editor()
        data = {
            'title': "Un titre",
            'publication': BaseArticle.PUBLISHED,
            'template': get_article_templates(None, self.user)[0][0],
            'navigation_parent': node1.id,
            'sites': [settings.SITE_ID]
        }
        
        response = self.client.post(reverse('coop_cms_new_article'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(article_class.objects.exclude(id=art1.id).count(), 1)
        art2 = article_class.objects.exclude(id=art1.id)[0]
        
        self.assertEqual(art2.title, data['title'])
        self.assertEqual(art2.publication, data['publication'])
        self.assertEqual(art2.template, data['template'])
        self.assertEqual(art2.navigation_parent, node1.id)
        
        self.assertEqual(NavNode.objects.count(), 2)
        node2 = NavNode.objects.exclude(id=node1.id)[0]
        self.assertEqual(node2.content_object, art2)
        self.assertEqual(node2.parent, node1)
        
    def test_article_settings(self, move_nav=False):
        initial_data = {'title': "test", 'content': "this is my article content"}
        article_class = get_article_class()
        art0 = mommy.make(article_class, slug="art0" )
        
        art1 = article_class.objects.create(publication=BaseArticle.PUBLISHED, **initial_data)
        
        tree = get_navtree_class().objects.create()
        ct = ContentType.objects.get_for_model(article_class)
        node1 = NavNode.objects.create(content_type=ct, object_id=art0.id, tree=tree, parent=None)
        node2 = NavNode.objects.create(content_type=ct, object_id=art0.id, tree=tree, parent=None)
        
        category = mommy.make(ArticleCategory)
        
        self._log_as_editor()
        data = {
            'template': get_article_templates(None, self.user)[0][0],
            'category': category.id,
            'publication': BaseArticle.PUBLISHED,
            'publication_date': "2013-01-01 12:00:00",
            'headline': True,
            'in_newsletter': True,
            'summary': 'short summary',
            'navigation_parent': node1.id,
            'sites': [settings.SITE_ID]
        }
        
        response = self.client.post(reverse('coop_cms_article_settings', args=[art1.id]), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(article_class.objects.exclude(id__in=(art1.id, art0.id)).count(), 0)
        art1 = article_class.objects.get(id=art1.id)
        
        self.assertEqual(art1.title, initial_data['title'])
        self.assertEqual(art1.publication, data['publication'])
        self.assertEqual(art1.navigation_parent, node1.id)
        self.assertEqual(art1.publication_date, make_dt(datetime(2013, 1, 1, 12, 0, 0)))
        self.assertEqual(art1.headline, data['headline'])
        self.assertEqual(art1.in_newsletter, data['in_newsletter'])
        self.assertEqual(art1.summary, data['summary'])
        self.assertEqual(art1.template, data['template'])
        self.assertEqual([a.id for a in art1.sites.all()], data['sites'])
        self.assertEqual(NavNode.objects.count(), 3)
        node = NavNode.objects.exclude(id__in=(node1.id, node2.id))[0]
        self.assertEqual(node.content_object, art1)
        self.assertEqual(node.parent, node1)
        
        # Update the article
        category2 = mommy.make(ArticleCategory)
        
        node_id = node2.id if move_nav else node1.id
        
        data = {
            'template': get_article_templates(None, self.user)[1][0],
            'category': category2.id,
            'publication': BaseArticle.DRAFT,
            'publication_date': "2013-01-01 18:00:00",
            'headline': False,
            'in_newsletter': False,
            'summary': 'another summary',
            'navigation_parent': node_id,
            'sites': [settings.SITE_ID]
        }
        
        response = self.client.post(reverse('coop_cms_article_settings', args=[art1.id]), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(article_class.objects.exclude(id__in=(art1.id, art0.id)).count(), 0)
        art1 = article_class.objects.get(id=art1.id)
        
        self.assertEqual(art1.title, initial_data['title'])
        self.assertEqual(art1.publication, data['publication'])
        self.assertEqual(art1.template, data['template'])
        self.assertEqual(art1.publication_date, make_dt(datetime(2013, 1, 1, 18, 0, 0)))
        self.assertEqual(art1.headline, data['headline'])
        self.assertEqual(art1.in_newsletter, data['in_newsletter'])
        self.assertEqual(art1.summary, data['summary'])

        if move_nav:
            self.assertEqual(NavNode.objects.count(), 4)
            node = NavNode.objects.exclude(id__in=(node1.id, node2.id, node.id))[0]
            self.assertEqual(node.content_object, art1)
            self.assertEqual(node.parent, node2)
        else:
            self.assertEqual(NavNode.objects.count(), 3)
            node = NavNode.objects.exclude(id__in=(node1.id, node2.id))[0]
            self.assertEqual(node.content_object, art1)
            self.assertEqual(node.parent, node1)
            
    def test_article_settings_move_nav(self):
        self.test_article_settings(True)

    def test_article_settings_on_two_sites(self):
        other_site = mommy.make(Site)

        initial_data = {'title': "test", 'content': "this is my article content"}
        article_class = get_article_class()

        art1 = article_class.objects.create(publication=BaseArticle.PUBLISHED, **initial_data)

        self._log_as_editor()
        data = {
            'template': get_article_templates(None, self.user)[0][0],
            'category': '',
            'publication': BaseArticle.PUBLISHED,
            'publication_date': "2013-01-01 12:00:00",
            'headline': True,
            'in_newsletter': True,
            'summary': 'short summary',
            'navigation_parent': None,
            'sites': [settings.SITE_ID, other_site.id]
        }

        response = self.client.post(reverse('coop_cms_article_settings', args=[art1.id]), data=data, follow=True)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(article_class.objects.exclude(id=art1.id).count(), 0)
        art1 = article_class.objects.get(id=art1.id)

        self.assertEqual(art1.summary, data['summary'])
        self.assertEqual(sorted([a.id for a in art1.sites.all()]), sorted(data['sites']))

    def test_article_settings_unknown_sites(self):
        other_site = mommy.make(Site)

        initial_data = {'title': "test", 'content': "this is my article content"}
        article_class = get_article_class()

        art1 = article_class.objects.create(publication=BaseArticle.PUBLISHED, **initial_data)

        self._log_as_editor()
        data = {
            'template': get_article_templates(None, self.user)[0][0],
            'category': '',
            'publication': BaseArticle.PUBLISHED,
            'publication_date': "2013-01-01 12:00:00",
            'headline': True,
            'in_newsletter': True,
            'summary': 'short summary',
            'navigation_parent': None,
            'sites': [settings.SITE_ID, 999]
        }

        response = self.client.post(reverse('coop_cms_article_settings', args=[art1.id]), data=data, follow=True)
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content)
        self.assertEqual(len(soup.select("ul.errorlist")), 1)

        self.assertEqual(article_class.objects.exclude(id=art1.id).count(), 0)
        art1 = article_class.objects.get(id=art1.id)

        self.assertNotEqual(art1.summary, data['summary'])
        self.assertEqual(sorted([a.id for a in art1.sites.all()]), [settings.SITE_ID])

    def test_article_settings_no_sites(self):
        other_site = mommy.make(Site)

        initial_data = {'title': "test", 'content': "this is my article content"}
        article_class = get_article_class()

        art1 = article_class.objects.create(publication=BaseArticle.PUBLISHED, **initial_data)

        self._log_as_editor()
        data = {
            'template': get_article_templates(None, self.user)[0][0],
            'category': '',
            'publication': BaseArticle.PUBLISHED,
            'publication_date': "2013-01-01 12:00:00",
            'headline': True,
            'in_newsletter': True,
            'summary': 'short summary',
            'navigation_parent': None,
            'sites': []
        }

        response = self.client.post(reverse('coop_cms_article_settings', args=[art1.id]), data=data, follow=True)
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content)
        self.assertEqual(len(soup.select("ul.errorlist")), 1)

        self.assertEqual(article_class.objects.exclude(id=art1.id).count(), 0)
        art1 = article_class.objects.get(id=art1.id)

        self.assertNotEqual(art1.summary, data['summary'])
        self.assertEqual(sorted([a.id for a in art1.sites.all()]), [settings.SITE_ID])

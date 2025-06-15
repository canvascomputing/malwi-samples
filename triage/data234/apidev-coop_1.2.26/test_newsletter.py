# -*- coding: utf-8 -*-

from datetime import timedelta
from unittest import skipIf

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core import mail
from django.core import management
from django.core.urlresolvers import reverse
from django.template import Template, Context
from django.test.utils import override_settings
from django.utils import timezone
from django.utils.translation import ugettext

from model_mommy import mommy

from coop_cms.models import Newsletter, NewsletterItem, PieceOfHtml, NewsletterSending
from coop_cms.settings import is_localized, get_article_class
from coop_cms.tests import BaseTestCase, UserBaseTestCase, BeautifulSoup
from coop_cms.utils import make_links_absolute, strip_a_tags, avoid_line_too_long, send_email


@override_settings(COOP_CMS_NEWSLETTER_SETTINGS_FORM='')
class NewsletterSettingsTest(UserBaseTestCase):

    def setUp(self):
        super(NewsletterSettingsTest, self).setUp()
        self._COOP_CMS_NEWSLETTER_TEMPLATES = getattr(settings, 'COOP_CMS_NEWSLETTER_TEMPLATES', None)
        settings.COOP_CMS_NEWSLETTER_TEMPLATES = (
            ('test/newsletter_blue.html', 'Blue'),
            ('test/newsletter_red.html', 'Blue'),
        )

    def tearDown(self):
        super(NewsletterSettingsTest, self).tearDown()
        settings.COOP_CMS_NEWSLETTER_TEMPLATES = self._COOP_CMS_NEWSLETTER_TEMPLATES

    def test_view_create_newsletter(self):
        self._log_as_editor()
        url = reverse("coop_cms_new_newsletter")

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(Newsletter.objects.count(), 0)

    def test_create_newsletter(self):
        self._log_as_editor()
        url = reverse("coop_cms_new_newsletter")

        data = {
            "subject": "test",
            "template": "test/newsletter_blue.html",
            'items': []
        }

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(Newsletter.objects.count(), 1)
        newsletter = Newsletter.objects.all()[0]

        self.assertEqual(newsletter.subject, data["subject"])
        self.assertEqual(newsletter.template, data["template"])

    def test_view_edit_newsletter(self):
        self._log_as_editor()
        newsletter = mommy.make(
            Newsletter,
            subject="a little intro for this newsletter",
            template="test/newsletter_blue.html",
        )

        url = reverse("coop_cms_newsletter_settings", args=[newsletter.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_newsletter(self):
        self._log_as_editor()
        newsletter = mommy.make(
            Newsletter,
            subject="a little intro for this newsletter",
            template="test/newsletter_red.html",
        )
        url = reverse("coop_cms_newsletter_settings", args=[newsletter.id])

        data = {
            "subject": "test",
            "template": "test/newsletter_blue.html",
            'items': []
        }

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(Newsletter.objects.count(), 1)
        newsletter = Newsletter.objects.all()[0]

        self.assertEqual(newsletter.subject, data["subject"])
        self.assertEqual(newsletter.template, data["template"])

    def test_view_newsletter_items(self):
        self._log_as_editor()
        article_class = get_article_class()

        site = Site.objects.get_current()
        other_site = mommy.make(Site)

        article_1 = mommy.make(article_class, slug="test1", in_newsletter=True)
        article_2 = mommy.make(article_class, slug="test2", in_newsletter=True, sites=[other_site])
        article_3 = mommy.make(article_class, slug="test3", in_newsletter=True)
        article_4 = mommy.make(article_class, slug="test4", in_newsletter=False)

        article_2.sites.clear()
        article_2.sites.add(other_site)
        article_2.save()

        ct = ContentType.objects.get_for_model(article_class)
        self.assertEqual(3, NewsletterItem.objects.count())
        item_1 = NewsletterItem.objects.get(content_type=ct, object_id=article_1.id)
        item_2 = NewsletterItem.objects.get(content_type=ct, object_id=article_2.id)
        item_3 = NewsletterItem.objects.get(content_type=ct, object_id=article_3.id)

        newsletter = mommy.make(
            Newsletter,
            subject="a little intro for this newsletter",
            template="test/newsletter_red.html",
            items=[item_1]
        )

        url = reverse("coop_cms_newsletter_settings", args=[newsletter.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content)

        options = soup.select("#id_items option")
        self.assertEqual(2, len(options))
        self.assertEqual(
            sorted([int(id_["value"]) for id_ in options]),
            sorted([item.id for item in [item_1, item_3]])
        )

        options = soup.select("#id_items option[selected=selected]")
        self.assertEqual(1, len(options))
        self.assertEqual(
            sorted([int(id_["value"]) for id_ in options]),
            sorted([item.id for item in [item_1]])
        )

    def test_save_newsletter_items(self):
        self._log_as_editor()
        article_class = get_article_class()

        site = Site.objects.get_current()
        other_site = mommy.make(Site)

        article_1 = mommy.make(article_class, slug="test1", in_newsletter=True)
        article_2 = mommy.make(article_class, slug="test2", in_newsletter=True)
        article_3 = mommy.make(article_class, slug="test3", in_newsletter=True)

        ct = ContentType.objects.get_for_model(article_class)
        self.assertEqual(3, NewsletterItem.objects.count())
        item_1 = NewsletterItem.objects.get(content_type=ct, object_id=article_1.id)
        item_2 = NewsletterItem.objects.get(content_type=ct, object_id=article_2.id)
        item_3 = NewsletterItem.objects.get(content_type=ct, object_id=article_3.id)

        newsletter = mommy.make(
            Newsletter,
            subject="a little intro for this newsletter",
            template="test/newsletter_red.html",
            items=[item_1]
        )

        data = {
            "subject": "test",
            "template": "test/newsletter_blue.html",
            'items': [item_2.id, item_3.id]
        }

        url = reverse("coop_cms_newsletter_settings", args=[newsletter.id])

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

        newsletter = Newsletter.objects.get(id=newsletter.id)
        self.assertEqual(newsletter.subject, data["subject"])
        self.assertEqual(newsletter.template, data["template"])
        self.assertEqual(
            list(sorted(n.id for n in newsletter.items.all())),
            list(sorted(data["items"]))
        )

    def test_save_newsletter_items_other_site(self):
        self._log_as_editor()
        article_class = get_article_class()

        site = Site.objects.get_current()
        other_site = mommy.make(Site)

        article_1 = mommy.make(article_class, slug="test1", in_newsletter=True)
        article_2 = mommy.make(article_class, slug="test2", in_newsletter=True)
        article_3 = mommy.make(article_class, slug="test3", in_newsletter=True)

        article_2.sites.clear()
        article_2.sites.add(other_site)
        article_2.save()

        content_type = ContentType.objects.get_for_model(article_class)
        self.assertEqual(3, NewsletterItem.objects.count())
        item_1 = NewsletterItem.objects.get(content_type=content_type, object_id=article_1.id)
        item_2 = NewsletterItem.objects.get(content_type=content_type, object_id=article_2.id)
        item_3 = NewsletterItem.objects.get(content_type=content_type, object_id=article_3.id)

        newsletter = mommy.make(
            Newsletter,
            subject="a little intro for this newsletter",
            template="test/newsletter_red.html",
            items=[item_1]
        )

        data = {
            "subject": "test",
            "template": "test/newsletter_blue.html",
            'items': [item_2.id, item_3.id]
        }

        url = reverse("coop_cms_newsletter_settings", args=[newsletter.id])

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content)

        self.assertEqual(len(soup.select(".errorlist")), 1)
        self.assertEqual(len(soup.select("#id_items")[0].parent.select(".errorlist")), 1)

        newsletter = Newsletter.objects.get(id=newsletter.id)
        self.assertNotEqual(newsletter.subject, data["subject"])
        self.assertNotEqual(newsletter.template, data["template"])
        self.assertEqual([item_1.id], [x.id for x in newsletter.items.all()])

    def test_save_newsletter_items_no_newsletter(self):
        self._log_as_editor()
        article_class = get_article_class()

        site = Site.objects.get_current()
        other_site = mommy.make(Site)

        article_1 = mommy.make(article_class, slug="test1", in_newsletter=True)
        article_2 = mommy.make(article_class, slug="test2", in_newsletter=True)
        article_3 = mommy.make(article_class, slug="test3", in_newsletter=True)

        content_type = ContentType.objects.get_for_model(article_class)
        self.assertEqual(3, NewsletterItem.objects.count())
        item_1 = NewsletterItem.objects.get(content_type=content_type, object_id=article_1.id)
        item_2 = NewsletterItem.objects.get(content_type=content_type, object_id=article_2.id)
        item_3 = NewsletterItem.objects.get(content_type=content_type, object_id=article_3.id)

        article_2.in_newsletter = False
        article_2.save()

        self.assertEqual(2, NewsletterItem.objects.count())

        newsletter = mommy.make(
            Newsletter,
            subject="a little intro for this newsletter",
            template="test/newsletter_red.html",
            items=[item_1]
        )

        data = {
            "subject": "test",
            "template": "test/newsletter_blue.html",
            'items': [item_2.id, item_3.id]
        }

        url = reverse("coop_cms_newsletter_settings", args=[newsletter.id])

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content)

        self.assertEqual(len(soup.select(".errorlist")), 1)
        self.assertEqual(len(soup.select("#id_items")[0].parent.select(".errorlist")), 1)

        newsletter = Newsletter.objects.get(id=newsletter.id)
        self.assertNotEqual(newsletter.subject, data["subject"])
        self.assertNotEqual(newsletter.template, data["template"])
        self.assertEqual([item_1.id], [x.id for x in newsletter.items.all()])

    def test_view_create_newsletter_not_logged(self):
        url = reverse("coop_cms_new_newsletter")

        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_create_newsletter_not_logged(self):
        url = reverse("coop_cms_new_newsletter")

        data = {
            "subject": "test",
            "template": "test/newsletter_blue.html",
            'items': []
        }

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

        self.assertEqual(Newsletter.objects.count(), 0)

    def test_view_edit_newsletter_not_logged(self):
        newsletter = mommy.make(
            Newsletter,
            subject="a little intro for this newsletter",
            template="test/newsletter_blue.html",
        )

        url = reverse("coop_cms_newsletter_settings", args=[newsletter.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_edit_newsletter_not_logged(self):
        subject = "a little intro for this newsletter"
        newsletter = mommy.make(
            Newsletter,
            subject=subject,
            template="test/newsletter_red.html",
        )
        url = reverse("coop_cms_newsletter_settings", args=[newsletter.id])

        data = {
            "subject": "test",
            "template": "test/newsletter_blue.html",
            'items': []
        }

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

        self.assertEqual(Newsletter.objects.count(), 1)
        newsletter = Newsletter.objects.all()[0]

        self.assertEqual(newsletter.subject, subject)


class NewsletterTest(UserBaseTestCase):

    def test_create_article_for_newsletter(self):
        article_class = get_article_class()
        content_type = ContentType.objects.get_for_model(article_class)
        
        art = mommy.make(article_class, slug="test", in_newsletter=True)
        
        self.assertEqual(1, NewsletterItem.objects.count())
        item = NewsletterItem.objects.get(content_type=content_type, object_id=art.id)
        self.assertEqual(item.content_object, art)
        
        art.delete()
        self.assertEqual(0, NewsletterItem.objects.count())

    def test_create_article_not_for_newsletter(self):
        article_class = get_article_class()
        ContentType.objects.get_for_model(article_class)
        
        art = mommy.make(article_class, slug="test", in_newsletter=False)
        self.assertEqual(0, NewsletterItem.objects.count())
        
        art.delete()
        self.assertEqual(0, NewsletterItem.objects.count())

    def test_create_article_commands(self):
        article_class = get_article_class()
        content_type = ContentType.objects.get_for_model(article_class)
        art1 = mommy.make(article_class, slug="test1", in_newsletter=True)
        art2 = mommy.make(article_class, slug="test2", in_newsletter=True)
        art3 = mommy.make(article_class, slug="test3", in_newsletter=False)
        self.assertEqual(2, NewsletterItem.objects.count())
        NewsletterItem.objects.all().delete()
        self.assertEqual(0, NewsletterItem.objects.count())
        management.call_command('create_newsletter_items', verbosity=0, interactive=False)
        self.assertEqual(2, NewsletterItem.objects.count())
        item1 = NewsletterItem.objects.get(content_type=content_type, object_id=art1.id)
        item2 = NewsletterItem.objects.get(content_type=content_type, object_id=art2.id)

    def test_view_newsletter(self):
        article_class = get_article_class()
        content_type = ContentType.objects.get_for_model(article_class)
        
        art1 = mommy.make(article_class, title="Art 1", in_newsletter=True)
        art2 = mommy.make(article_class, title="Art 2", in_newsletter=True)
        art3 = mommy.make(article_class, title="Art 3", in_newsletter=True)
        
        newsletter = mommy.make(
            Newsletter,
            content="a little intro for this newsletter",
            template="test/newsletter_blue.html",
            is_public=True
        )
        newsletter.items.add(NewsletterItem.objects.get(content_type=content_type, object_id=art1.id))
        newsletter.items.add(NewsletterItem.objects.get(content_type=content_type, object_id=art2.id))
        newsletter.save()
        
        url = reverse('coop_cms_view_newsletter', args=[newsletter.id])
        response = self.client.get(url)
        
        self.assertEqual(200, response.status_code)
        
        self.assertContains(response, newsletter.content)
        self.assertContains(response, art1.title)
        self.assertContains(response, art2.title)
        self.assertNotContains(response, art3.title)

    def test_view_newsletter_not_public(self):

        newsletter = mommy.make(
            Newsletter,
            content="a little intro for this newsletter",
            template="test/newsletter_blue.html",
        )

        url = reverse('coop_cms_view_newsletter', args=[newsletter.id])
        response = self.client.get(url)

        self.assertEqual(403, response.status_code)
        
    def test_edit_newsletter_is_public(self):
        newsletter = mommy.make(
            Newsletter,
            content="a little intro for this newsletter",
            template="test/newsletter_blue.html",
            is_public=True
        )

        self._log_as_editor()
        url = reverse('coop_cms_edit_newsletter', args=[newsletter.id])
        response = self.client.get(url)
        
        self.assertEqual(200, response.status_code)
        
        data = {'content': 'A better intro'}
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(200, response.status_code)
        
        self.assertNotContains(response, newsletter.content)
        self.assertContains(response, data['content'])

    def test_edit_newsletter_not_public(self):
        newsletter = mommy.make(
            Newsletter,
            content="a little intro for this newsletter",
            template="test/newsletter_blue.html",
            is_public=False
        )

        self._log_as_editor()
        url = reverse('coop_cms_edit_newsletter', args=[newsletter.id])
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)

        data = {'content': 'A better intro'}
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(200, response.status_code)

        self.assertNotContains(response, newsletter.content)
        self.assertContains(response, data['content'])

    def test_edit_newsletter_anonymous(self):
        original_data = {
            'content': "a little intro for this newsletter",
            'template': "test/newsletter_blue.html"
        }
        newsletter = mommy.make(Newsletter, **original_data)
        
        url = reverse('coop_cms_edit_newsletter', args=[newsletter.id])
        response = self.client.get(url)
        self.assertEqual(403, response.status_code)
        
        response = self.client.post(url, data={'content': ':OP'})
        self.assertEqual(403, response.status_code)
        
        newsletter = Newsletter.objects.get(id=newsletter.id)
        self.assertEqual(newsletter.content, original_data['content'])
        
    def test_edit_newsletter_no_articles(self):
        self._log_as_editor()
        original_data = {
            'content': "a little intro for this newsletter",
            'template': "test/newsletter_blue.html"
        }
        newsletter = mommy.make(Newsletter, **original_data)
        
        url = reverse('coop_cms_edit_newsletter', args=[newsletter.id])
        
        data = {'content': ':OP'}
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, data['content'])
        
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, data['content'])
        
    def test_newsletter_templates(self):
        """it should send email with right content"""
        article_class = get_article_class()
        content_type = ContentType.objects.get_for_model(article_class)
        
        art1 = mommy.make(article_class, title="Art 1", in_newsletter=True)
        poh = mommy.make(PieceOfHtml, div_id="newsletter_header", content="HELLO!!!")
        
        newsletter = mommy.make(
            Newsletter,
            content="a little intro for this newsletter",
            template="test/newsletter_blue.html"
        )
        newsletter.items.add(NewsletterItem.objects.get(content_type=content_type, object_id=art1.id))
        newsletter.save()
        
        self._log_as_editor()
        
        view_names = ['coop_cms_view_newsletter', 'coop_cms_edit_newsletter']
        for view_name in view_names:

            url = reverse(view_name, args=[newsletter.id])
            response = self.client.get(url)
            self.assertEqual(200, response.status_code)

            self.assertContains(response, newsletter.content)
            self.assertContains(response, art1.title)
            self.assertContains(response, "background: blue;")
            self.assertNotContains(response, poh.content)
        
        newsletter.template = "test/newsletter_red.html"
        newsletter.save()
        
        for view_name in view_names:
            url = reverse(view_name, args=[newsletter.id])
            response = self.client.get(url)
            
            self.assertEqual(200, response.status_code)
            
            self.assertContains(response, newsletter.content)
            self.assertContains(response, art1.title)
            self.assertContains(response, "background: red;")
            self.assertContains(response, poh.content)
            
    def test_change_newsletter_templates(self):
        settings.COOP_CMS_NEWSLETTER_TEMPLATES = (
            ('test/newsletter_red.html', 'Red'),
            ('test/newsletter_blue.html', 'Blue'),
        )
        self._log_as_editor()
        
        newsletter = mommy.make(Newsletter, template='test/newsletter_blue.html')
        
        url = reverse('coop_cms_change_newsletter_template', args=[newsletter.id])
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        
        for tpl, name in settings.COOP_CMS_NEWSLETTER_TEMPLATES:
            self.assertContains(response, tpl)
            self.assertContains(response, name)
            
        data={'template': 'test/newsletter_red.html'}
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, reverse('coop_cms_edit_newsletter', args=[newsletter.id]))
        
        newsletter = Newsletter.objects.get(id=newsletter.id)
        self.assertEqual(newsletter.template, data['template'])
        
    def test_change_newsletter_templates_anonymous(self):
        settings.COOP_CMS_NEWSLETTER_TEMPLATES = (
            ('test/newsletter_red.html', 'Red'),
            ('test/newsletter_blue.html', 'Blue'),
        )
        original_data={'template': 'test/newsletter_blue.html'}
        newsletter = mommy.make(Newsletter, **original_data)
        
        url = reverse('coop_cms_change_newsletter_template', args=[newsletter.id])
        response = self.client.get(url)
        self.assertEqual(302, response.status_code)
        
        data={'template': 'test/newsletter_red.html'}
        response = self.client.post(url, data=data)
        self.assertEqual(302, response.status_code)
        
        newsletter = Newsletter.objects.get(id=newsletter.id)
        self.assertEqual(newsletter.template, original_data['template'])
        
    def test_change_newsletter_unknow_template(self):
        settings.COOP_CMS_NEWSLETTER_TEMPLATES = (
            ('test/newsletter_red.html', 'Red'),
            ('test/newsletter_blue.html', 'Blue'),
        )
        original_data={'template': 'test/newsletter_blue.html'}
        newsletter = mommy.make(Newsletter, **original_data)
        
        self._log_as_editor()
        url = reverse('coop_cms_change_newsletter_template', args=[newsletter.id])
        data={'template': 'test/newsletter_yellow.html'}
        response = self.client.post(url, data=data)
        self.assertEqual(200, response.status_code)
        
        newsletter = Newsletter.objects.get(id=newsletter.id)
        self.assertEqual(newsletter.template, original_data['template'])

    @override_settings(COOP_CMS_TEST_EMAILS=['toto@toto.fr', 'titi@toto.fr'], COOP_CMS_FROM_EMAIL='contact@toto.fr')
    def test_send_test_newsletter(self, template='test/newsletter_blue.html', extra_checker=None):
        settings.SITE_ID = 1
        site = Site.objects.get(id=settings.SITE_ID)
        site.domain = 'toto.fr'
        site.save()
        
        rel_content = u'''
            <h1>Title</h1><a href="{0}/toto/"><img src="{0}/toto.jpg"></a><br /><img src="{0}/toto.jpg">
            <div><a href="http://www.google.fr">Google</a></div>
        '''
        original_data = {
            'template': template,
            'subject': 'test email',
            'content': rel_content.format("")
        }
        newsletter = mommy.make(Newsletter, **original_data)
        
        self._log_as_editor()
        url = reverse('coop_cms_test_newsletter', args=[newsletter.id])
        response = self.client.post(url, data={})
        self.assertEqual(200, response.status_code)
        
        self.assertEqual(
            [[test_address] for test_address in settings.COOP_CMS_TEST_EMAILS],
            [received_email.to for received_email in mail.outbox]
        )
        for received_email in mail.outbox:
            self.assertEqual(received_email.from_email, settings.COOP_CMS_FROM_EMAIL)
            self.assertEqual(received_email.subject, newsletter.subject)
            self.assertTrue(received_email.body.find('Title') >= 0)
            self.assertTrue(received_email.body.find('Google') >= 0)
            self.assertTrue(received_email.alternatives[0][1], "text/html")
            self.assertTrue(received_email.alternatives[0][0].find('Title') >= 0)
            self.assertTrue(received_email.alternatives[0][0].find('Google') >= 0)
            site_prefix = "http://"+site.domain
            self.assertTrue(received_email.alternatives[0][0].find(site_prefix) >= 0)
            if extra_checker:
                extra_checker(received_email)
        
    def test_schedule_newsletter_sending(self):
        newsletter = mommy.make(Newsletter)
        
        self._log_as_editor()
        url = reverse('coop_cms_schedule_newsletter_sending', args=[newsletter.id])
        
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        
        sch_dt = "2030-12-12 12:00:00"
        response = self.client.post(url, data={'scheduling_dt': sch_dt})
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '$.colorbox.close()')
        self.assertEqual(1, NewsletterSending.objects.count())
        self.assertEqual(newsletter, NewsletterSending.objects.all()[0].newsletter)
        self.assertEqual(2030, NewsletterSending.objects.all()[0].scheduling_dt.year)
        
    def test_schedule_newsletter_sending_invalid_value(self):
        newsletter = mommy.make(Newsletter)
        
        self._log_as_editor()
        url = reverse('coop_cms_schedule_newsletter_sending', args=[newsletter.id])
        
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        
        sch_dt = ''
        response = self.client.post(url, data={'scheduling_dt': sch_dt})
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, NewsletterSending.objects.count())
        
        sch_dt = 'toto'
        response = self.client.post(url, data={'scheduling_dt': sch_dt})
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, NewsletterSending.objects.count())
        
        sch_dt = "2005-12-12 12:00:00"
        response = self.client.post(url, data={'scheduling_dt': sch_dt})
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, NewsletterSending.objects.count())
    
    def test_schedule_anonymous(self):
        newsletter = mommy.make(Newsletter)
        
        login_url = reverse('django.contrib.auth.views.login')
        url = reverse('coop_cms_schedule_newsletter_sending', args=[newsletter.id])
        
        response = self.client.get(url, follow=False)
        redirect_url = response['Location']
        if is_localized():
            login_url = login_url[:2]
            self.assertTrue(redirect_url.find(login_url) >= 0)
        else:
            self.assertTrue(redirect_url.find(login_url) >= 0)
        
        sch_dt = timezone.now()+timedelta(1)
        response = self.client.post(url, data={'sending_dt': sch_dt})
        redirect_url = response['Location']
        self.assertTrue(redirect_url.find(login_url) >= 0)
    
    def test_send_newsletter(self):
        
        newsletter_data = {
            'subject': 'This is the subject',
            'content': '<h2>Hello guys!</h2><p>Visit <a href="http://toto.fr">us</a></p>',
            'template': 'test/newsletter_blue.html',
        }
        newsletter = mommy.make(Newsletter, **newsletter_data)
        self.assertEqual(newsletter.is_public, False)
        sch_dt = timezone.now() - timedelta(1)
        sending = mommy.make(NewsletterSending, newsletter=newsletter, scheduling_dt= sch_dt, sending_dt= None)

        management.call_command('send_newsletter', 'toto@toto.fr', verbosity=0, interactive=False)

        sending = NewsletterSending.objects.get(id=sending.id)
        self.assertNotEqual(sending.sending_dt, None)
        
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.to, ['toto@toto.fr'])
        self.assertEqual(email.subject, newsletter_data['subject'])
        self.assertTrue(email.body.find('Hello guys') >= 0)
        self.assertTrue(email.alternatives[0][1], "text/html")
        self.assertTrue(email.alternatives[0][0].find('Hello guys') >= 0)

        newsletter = Newsletter.objects.get(id=newsletter.id)
        self.assertEqual(newsletter.is_public, True)
        
        # check whet happens if command is called again
        mail.outbox = []
        management.call_command('send_newsletter', 'toto@toto.fr', verbosity=0, interactive=False)
        self.assertEqual(len(mail.outbox), 0)

    def test_send_newsletter_several(self):
        """it should send newsletter to several addresses"""

        newsletter_data = {
            'subject': 'This is the subject',
            'content': '<h2>Hello guys!</h2><p>Visit <a href="http://toto.fr">us</a></p>',
            'template': 'test/newsletter_blue.html',
        }
        newsletter = mommy.make(Newsletter, **newsletter_data)
        
        sch_dt = timezone.now() - timedelta(1)
        sending = mommy.make(NewsletterSending, newsletter=newsletter, scheduling_dt= sch_dt, sending_dt= None)
        
        addresses = ';'.join(['toto@toto.fr']*5)
        management.call_command('send_newsletter', addresses, verbosity=0, interactive=False)
        
        sending = NewsletterSending.objects.get(id=sending.id)
        self.assertNotEqual(sending.sending_dt, None)
        
        self.assertEqual(len(mail.outbox), 5)
        for email in mail.outbox:
            self.assertEqual(email.to, ['toto@toto.fr'])
            self.assertEqual(email.subject, newsletter_data['subject'])
            self.assertTrue(email.body.find('Hello guys')>=0)
            self.assertTrue(email.alternatives[0][1], "text/html")
            self.assertTrue(email.alternatives[0][0].find('Hello guys')>=0)
        
        # check whet happens if command is called again
        mail.outbox = []
        management.call_command('send_newsletter', 'toto@toto.fr', verbosity=0, interactive=False)
        self.assertEqual(len(mail.outbox), 0)

    def test_send_newsletter_not_yet(self):
        
        newsletter_data = {
            'subject': 'This is the subject',
            'content': '<h2>Hello guys!</h2><p>Visit <a href="http://toto.fr">us</a></p>',
            'template': 'test/newsletter_blue.html',
        }
        newsletter = mommy.make(Newsletter, **newsletter_data)
        
        sch_dt = timezone.now() + timedelta(1)
        sending = mommy.make(NewsletterSending, newsletter=newsletter, scheduling_dt= sch_dt, sending_dt= None)
        
        management.call_command('send_newsletter', 'toto@toto.fr', verbosity=0, interactive=False)
        
        sending = NewsletterSending.objects.get(id=sending.id)
        self.assertEqual(sending.sending_dt, None)
        
        self.assertEqual(len(mail.outbox), 0)


@override_settings(COOP_CMS_FROM_EMAIL='contact@toto.fr')
class SendEmailTest(UserBaseTestCase):
    """test utils.send_email"""

    def test_send_email(self):
        settings.SITE_ID = 1
        site = Site.objects.get(id=settings.SITE_ID)
        site.domain = 'toto.fr'
        site.save()

        site2 = mommy.make(Site, domain="toto.com")

        # subject, template_name, context, site_domain, dests, lang = None, list_unsubscribe = None

        subject = "Hello"
        dests = ['toto@toto.fr']

        send_email(subject, "test/test_send_email.html", {'value': 'ABCD'}, "http://" + site2.domain, dests)

        self.assertEqual(
            [[test_address] for test_address in dests],
            [received_email.to for received_email in mail.outbox]
        )
        for received_email in mail.outbox:
            self.assertEqual(received_email.from_email, settings.COOP_CMS_FROM_EMAIL)
            self.assertEqual(received_email.subject, subject)
            self.assertTrue(received_email.body.find('ABCD') >= 0)
            self.assertTrue(received_email.alternatives[0][1], "text/html")
            self.assertTrue(received_email.alternatives[0][0].find('ABCD') >= 0)
            site_prefix = "http://" + site2.domain
            self.assertTrue(received_email.alternatives[0][0].find(site_prefix) >= 0)

    @skipIf('en' not in [lang_code for (lang_code, lang_name) in settings.LANGUAGES], 'English required for this test')
    def test_send_email_en(self):
        settings.SITE_ID = 1
        site = Site.objects.get(id=settings.SITE_ID)
        site.domain = 'toto.fr'
        site.save()

        site2 = mommy.make(Site, domain="toto.com")

        # subject, template_name, context, site_domain, dests, lang = None, list_unsubscribe = None

        subject = "Hello"
        dests = ['toto@toto.fr']

        send_email(subject, "test/test_send_email.html", {'value': 'ABCD'}, "http://" + site2.domain, dests, 'en')

        self.assertEqual(
            [[test_address] for test_address in dests],
            [received_email.to for received_email in mail.outbox]
        )
        for received_email in mail.outbox:

            translated = 'All'  # ugettext('All')

            self.assertEqual(received_email.from_email, settings.COOP_CMS_FROM_EMAIL)
            self.assertEqual(received_email.subject, subject)
            self.assertTrue(received_email.body.find('ABCD') >= 0)
            self.assertTrue(received_email.body.find(translated) >= 0)
            self.assertTrue(received_email.alternatives[0][1], "text/html")
            self.assertTrue(received_email.alternatives[0][0].find('ABCD') >= 0)
            self.assertTrue(received_email.alternatives[0][0].find(translated) >= 0)
            site_prefix = "http://" + site2.domain
            self.assertTrue(received_email.alternatives[0][0].find(site_prefix) >= 0)

    @skipIf('fr' not in [lang_code for (lang_code, lang_name) in settings.LANGUAGES], 'French required for this test')
    def test_send_email_fr(self):
        settings.SITE_ID = 1
        site = Site.objects.get(id=settings.SITE_ID)
        site.domain = 'toto.fr'
        site.save()

        site2 = mommy.make(Site, domain="toto.com")

        # subject, template_name, context, site_domain, dests, lang = None, list_unsubscribe = None

        subject = "Hello"
        dests = ['toto@toto.fr']

        send_email(subject, "test/test_send_email.html", {'value': 'ABCD'}, "http://" + site2.domain, dests, 'fr')

        self.assertEqual(
            [[test_address] for test_address in dests],
            [received_email.to for received_email in mail.outbox]
        )
        for received_email in mail.outbox:
            translated = 'Tous'  # ugettext('All')

            self.assertEqual(received_email.from_email, settings.COOP_CMS_FROM_EMAIL)
            self.assertEqual(received_email.subject, subject)
            self.assertTrue(received_email.body.find('ABCD') >= 0)
            self.assertTrue(received_email.body.find(translated) >= 0)
            self.assertTrue(received_email.alternatives[0][1], "text/html")
            self.assertTrue(received_email.alternatives[0][0].find('ABCD') >= 0)
            self.assertTrue(received_email.alternatives[0][0].find(translated) >= 0)
            site_prefix = "http://" + site2.domain
            self.assertTrue(received_email.alternatives[0][0].find(site_prefix) >= 0)

    @skipIf('sn' in [lang_code for (lang_code, lang_name) in settings.LANGUAGES], 'No Chinese for this test')
    def test_send_email_sn(self):
        settings.SITE_ID = 1
        site = Site.objects.get(id=settings.SITE_ID)
        site.domain = 'toto.fr'
        site.save()

        site2 = mommy.make(Site, domain="toto.com")

        # subject, template_name, context, site_domain, dests, lang = None, list_unsubscribe = None

        subject = "Hello"
        dests = ['toto@toto.fr']

        send_email(subject, "test/test_send_email.html", {'value': 'ABCD'}, "http://" + site2.domain, dests, 'sn')

        self.assertEqual(
            [[test_address] for test_address in dests],
            [received_email.to for received_email in mail.outbox]
        )
        for received_email in mail.outbox:
            translated = 'All'  # ugettext('All')

            self.assertEqual(received_email.from_email, settings.COOP_CMS_FROM_EMAIL)
            self.assertEqual(received_email.subject, subject)
            self.assertTrue(received_email.body.find('ABCD') >= 0)
            self.assertTrue(received_email.body.find(translated) >= 0)
            self.assertTrue(received_email.alternatives[0][1], "text/html")
            self.assertTrue(received_email.alternatives[0][0].find('ABCD') >= 0)
            self.assertTrue(received_email.alternatives[0][0].find(translated) >= 0)
            site_prefix = "http://" + site2.domain
            self.assertTrue(received_email.alternatives[0][0].find(site_prefix) >= 0)


class AbsUrlTest(UserBaseTestCase):
    
    def setUp(self):
        super(AbsUrlTest, self).setUp()
        settings.SITE_ID = 1
        self.site = Site.objects.get(id=settings.SITE_ID)
        self.site.domain = "toto.fr"
        self.site.save()
        self.site_prefix = "http://"+self.site.domain
        self.newsletter = mommy.make(Newsletter, site=self.site)
        #settings.COOP_CMS_SITE_PREFIX = self.site_prefix

    def _to_text(self, soup):
        text = soup.prettify()
        text = strip_a_tags(text)
        return text
    
    def test_href(self):
        test_html = '<a href="%s/toto">This is a link</a>'
        rel_html = test_html % ""
        abs_html = self._to_text(BeautifulSoup(test_html % self.site_prefix))
        self.assertEqual(abs_html, strip_a_tags(make_links_absolute(rel_html, self.newsletter)))
        
    def test_src(self):
        test_html = '<h1>My image</h1><img src="%s/toto">'
        rel_html = test_html % ""
        abs_html = self._to_text(BeautifulSoup(test_html % self.site_prefix))
        self.assertEqual(abs_html, strip_a_tags(make_links_absolute(rel_html, self.newsletter)))
        
    def test_relative_path(self):
        test_html = '<h1>My image</h1><img src="%s/toto">'
        rel_html = test_html % "../../.."
        abs_html = self._to_text(BeautifulSoup(test_html % self.site_prefix))
        self.assertEqual(abs_html, strip_a_tags(make_links_absolute(rel_html, self.newsletter)))
    
    def test_src_and_img(self):
        test_html = '<h1>My image</h1><a href="{0}/a1">This is a link</a><img src="{0}/toto"/><img src="{0}/titi"/>' + \
            '<a href="{0}/a2">This is another link</a>'
        rel_html = test_html.format("")
        html = test_html.format(self.site_prefix)
        abs_html = self._to_text(BeautifulSoup(html))
        self.assertEqual(abs_html, strip_a_tags(make_links_absolute(rel_html, self.newsletter)))
        
    def test_href_rel_and_abs(self):
        test_html = '<a href="%s/toto">This is a link</a><a href="http://www.apidev.fr">another</a>'
        rel_html = test_html % ""
        abs_html = self._to_text(BeautifulSoup(test_html % self.site_prefix))
        self.assertEqual(abs_html, strip_a_tags(make_links_absolute(rel_html, self.newsletter)))
        
    def test_style_in_between(self):
        test_html = u'<img style="margin: 0; width: 700px;" src="%s/media/img/newsletter_header.png" alt="Logo">'
        rel_html = test_html % ""
        abs_html = self._to_text(BeautifulSoup(test_html % self.site_prefix))
        self.assertEqual(abs_html, strip_a_tags(make_links_absolute(rel_html, self.newsletter)))
        
    def test_missing_attr(self):
        test_html = u'<img alt="Logo" /><a name="aa">link</a>'
        abs_html = self._to_text(BeautifulSoup(test_html))
        self.assertEqual(abs_html, strip_a_tags(make_links_absolute(test_html, self.newsletter)))


class NewsletterFriendlyTemplateTagsTest(BaseTestCase):
    
    template_content = """
        {{% load coop_utils %}}
        {{% nlf_css {0} %}}
            <a>One</a>
            <a>Two</a>
            <a>Three</a>
            <img />
            <table><tr><td></td><td></td></table>
            <table class="this-one"><tr><td></td><td></td></table>
        {{% end_nlf_css %}}
    """
    
    def test_email_mode_is_inline(self):
        template = self.template_content.format('a="color: red;"')
        tpl = Template(template)
        html = tpl.render(Context({'by_email': True}))
        self.assertEqual(0, html.count(u'<style>'))
        self.assertEqual(3, html.count(u'<a style="color: red;">'))
        
    def test_edit_mode_is_in_style(self):
        template = self.template_content.format('a="color: red;"')
        tpl = Template(template)
        html = tpl.render(Context({'by_email': False}))
        self.assertEqual(1, html.count(u'<style>'))
        self.assertEqual(1, html.count(u'a { color: red; }'))
        self.assertEqual(0, html.count(u'<a style="color: red;">'))
        
    def test_several_args_email_mode_is_inline(self):
        template = self.template_content.format(
            'a="color: red; background: blue;" td="border: none;" img="width: 100px;"'
        )
        tpl = Template(template)
        html = tpl.render(Context({'by_email': True}))
        self.assertEqual(0, html.count(u'<style>'))
        self.assertEqual(3, html.count(u'<a style="color: red; background: blue;">'))
        self.assertEqual(1, html.count(u'<img style="width: 100px;"/>'))
        self.assertEqual(4, html.count(u'<td style="border: none;">'))
        
    def test_several_args_edit_mode_is_in_style(self):
        template = self.template_content.format(
            'a="color: red; background: blue;" td="border: none;" img="width: 100px;"'
        )
        tpl = Template(template)
        html = tpl.render(Context({'by_email': False}))
        self.assertEqual(1, html.count(u'<style>'))
        self.assertEqual(1, html.count(u'a { color: red; background: blue; }'))
        self.assertEqual(1, html.count(u'img { width: 100px; }'))
        self.assertEqual(1, html.count(u'td { border: none; }'))
        self.assertEqual(0, html.count(u'<a style="color: red; background: blue;">'))
        self.assertEqual(0, html.count(u'<img style="width: 100px;">'))
        self.assertEqual(0, html.count(u'<td style="border: none;">'))
        
    def test_class_selector_email_mode_is_inline(self):
        template = self.template_content.format('"table.this-one td"="border: none;"')
        tpl = Template(template)
        html = tpl.render(Context({'by_email': True}))
        self.assertEqual(0, html.count(u'<style>'))
        self.assertEqual(0, html.count(u'<a style="color: red; background: blue;">'))
        self.assertEqual(0, html.count(u'<img style="width: 100px;"/>'))
        self.assertEqual(2, html.count(u'<td style="border: none;">'))

    def test_dont_overwrite_inline(self):

        template_content = """
            {{% load coop_utils %}}
            {{% nlf_css {0} %}}
                <a style="color: #fff">One</a>
                <a>Two</a>
            {{% end_nlf_css %}}
        """

        template = template_content.format('a="color: red; background: blue;"')
        tpl = Template(template)
        html = tpl.render(Context({'by_email': True}))
        self.assertEqual(1, html.count(u'<a style="color: red; background: blue;">'))
        self.assertEqual(1, html.count(u'<a style="color: #fff; background: blue;">'))

    def test_keep_order_inline(self):

        template_content = """
            {{% load coop_utils %}}
            {{% nlf_css {0} %}}
                <a style="background: #000; color: #fff;">One</a>
                <a>Two</a>
            {{% end_nlf_css %}}
        """

        template = template_content.format('a="color: red; background: blue; padding: 0;"')
        tpl = Template(template)
        html = tpl.render(Context({'by_email': True}))

        self.assertEqual(1, html.count(u'<a style="background: #000; color: #fff; padding: 0;">'))
        self.assertEqual(1, html.count(u'<a style="color: red; background: blue; padding: 0;">'))

    def test_accept_quote(self):

        template_content = """
            {{% load coop_utils %}}
            {{% nlf_css {0} %}}
                <a style="font-family: 'Arial';">One</a>
                <a>Two</a>
            {{% end_nlf_css %}}
        """

        template = template_content.format('''a="font-family: 'Tahoma';"''')
        tpl = Template(template)
        html = tpl.render(Context({'by_email': True}))
        self.assertEqual(1, html.count(u'''<a style="font-family: 'Arial';">'''))
        self.assertEqual(1, html.count(u'''<a style="font-family: 'Tahoma';">'''))

    def test_css_order(self):

        template_content = """
            {{% load coop_utils %}}
            {{% nlf_css {0} %}}
                <a>One</a>
                <div class="blue">
                <a>Two</a>
                </div>
            {{% end_nlf_css %}}
        """

        tpl = Template(template_content.format('a="color: #000" ".blue a"="color: #fff"'))
        html = tpl.render(Context({'by_email': True}))
        self.assertEqual(2, html.count(u'''<a style="color: #000;">'''))
        self.assertEqual(0, html.count(u'''<a style="color: #fff';">'''))

        tpl = Template(template_content.format('".blue a"="color: #fff" a="color: #000"'))
        html = tpl.render(Context({'by_email': True}))
        self.assertEqual(1, html.count(u'''<a style="color: #000;">'''))
        self.assertEqual(1, html.count(u'''<a style="color: #fff;">'''))

    def test_no_end_tag(self):

        template_content = """
            {{% load coop_utils %}}
            {{% nlf_css {0} %}}
                <a>One</a>
                <hr />
                <a>Two</a>
            {{% end_nlf_css %}}
        """

        template = template_content.format('hr="color: red;"')
        tpl = Template(template)
        html = tpl.render(Context({'by_email': True}))
        self.assertEqual(1, html.count(u'<hr style="color: red;"/>'))


class HtmlFixTest(BaseTestCase):
    """Test dirty fixs for newsletter html"""

    def test_strip_a_tags(self):
        """Make sure that the a tags have no space inside"""
        html = u'''
        <p>
         <h1>Test</h1>
         <a class="link" href="/">
          Cool
         </a>
         <div>
         <a href="/test">
          Test
         </a>
         </div>
        </p>
        '''

        soup = BeautifulSoup(html)
        fixed_html = strip_a_tags(soup.prettify())

        expected_html = '<p>\n <h1>\n  Test\n </h1>\n <a class="link" href="/">Cool</a>\n <div>\n  ' \
        '<a href="/test">Test</a>\n </div>\n</p>\n'

        self.assertEqual(fixed_html, expected_html)

    def test_no_a_tags(self):
        """Make sure that content is returned properly if no a tag in content"""
        html = u'''
        <p>
         <h1>Test</h1>
        </p>
        '''

        soup = BeautifulSoup(html)
        fixed_html = strip_a_tags(soup.prettify())

        expected_html = '<p>\n <h1>\n  Test\n </h1>\n</p>\n'

        self.assertEqual(fixed_html, expected_html)

    def test_avoid_line_too_long(self):
        """newsletter should not contains more than 998 chars. Force some endline if so"""
        html = u'''
        <p>
         <h1>Test</h1>
         <a class="link" href="/">
          {0}
         </a>
         <div>
         <a href="/test">
          <h2>Eté</h2>
         </a>
         </div>
        </p>
        '''.format('abcd ' * 300)  # 1500

        fixed_html = avoid_line_too_long(html)

        max_length = 0
        for line in fixed_html.split('\n'):
            max_length = max(max_length, len(line))

        self.assertEqual(fixed_html.count('abcd'), 300)
        self.assertEqual(len(fixed_html.splitlines()), len(html.splitlines()) + 1 + (1500 // 900))
        self.assertTrue(max_length <= 900)
        self.assertTrue(fixed_html.find(u'<h1>Test</h1>') > 0)
        self.assertTrue(fixed_html.find(u'<h2>Eté</h2>') > 0)

    def test_avoid_line_very_too_long(self):
        """newsletter should not contains more than 998 chars. Force some endline if so"""
        html = u'''
        <p>
         <h1>Test</h1>
         <a class="link" href="/">
          {0}
         </a>
         <div>
         <a href="/test">
          <h2>Eté</h2>
         </a>
         </div>
        </p>
        '''.format(u'abcdé ' * 600)  # 4200 characters

        fixed_html = avoid_line_too_long(html)

        max_length = 0
        for line in fixed_html.split('\n'):
            max_length = max(max_length, len(line))

        self.assertEqual(fixed_html.count(u'abcdé'), 600)
        self.assertEqual(len(fixed_html.splitlines()), len(html.splitlines()) + 1 + (4200 // 900))
        self.assertTrue(max_length <= 900)
        self.assertTrue(fixed_html.find(u'<h1>Test</h1>') > 0)
        self.assertTrue(fixed_html.find(u'<h2>Eté</h2>') > 0)

    def test_avoid_line_too_long_no_change(self):
        """newsletter should not contains more than 998 chars. Force some endline if so"""
        html = u'''
        <p>
         <h1>Test</h1>
         <a class="link" href="/">
          Cool
         </a>
         <div>
         <a href="/test">
          Test
         </a>
         </div>
        </p>
        '''

        fixed_html = avoid_line_too_long(html)
        self.assertEqual(fixed_html, html)

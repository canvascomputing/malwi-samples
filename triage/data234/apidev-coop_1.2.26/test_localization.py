# -*- coding: utf-8 -*-
"""unit test i18n support"""

from django.conf import settings

from unittest import skipIf

from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.utils.translation import activate, get_language
from django.test.utils import override_settings

from coop_cms.models import BaseArticle, InvalidArticleError
from coop_cms.settings import is_localized, is_multilang, multilang_mode, get_article_class
from coop_cms.tests import BaseTestCase, BeautifulSoup
from coop_cms.utils import redirect_to_language, strip_locale_path, get_url_in_language, make_locale_path


def language_fallbacks():
    """return fallback"""
    return tuple([lang_code for (lang_code, lang_name) in settings.LANGUAGES])


@skipIf(not is_localized(), "not localized")
class LocalePathTest(BaseTestCase):
    """test that url is parsed correctly when using locale prefix"""

    def test_get_locale_article(self):
        """it should return lang and locale-independent-path"""
        result = strip_locale_path('/en/home/')
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 'en')
        self.assertEqual(result[1], '/home/')

    def test_get_locale_article_no_trailing(self):
        """it should return lang and locale-independent-path"""
        result = strip_locale_path('/en/home')
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 'en')
        self.assertEqual(result[1], '/home')

    def test_get_locale_article_no_prefix(self):
        """it should returns empty locale and path"""
        result = strip_locale_path('/home/')
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], '')
        self.assertEqual(result[1], '/home/')

    def test_get_locale_article_no_prefix_no_trailing(self):
        """it should returns empty locale and path"""
        result = strip_locale_path('/home')
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], '')
        self.assertEqual(result[1], '/home')

    @skipIf(not is_multilang(), "not multi lang")
    def test_get_url_in_language(self):
        """it should return url in another language"""

        origin_lang = settings.LANGUAGES[0][0]
        trans_lang = settings.LANGUAGES[1][0]

        activate(origin_lang)
        path = '/this-is-test/'
        origin_url = make_locale_path(path, origin_lang)

        trans_url = get_url_in_language(origin_url, trans_lang)
        self.assertEqual(trans_url, make_locale_path(path, trans_lang))


class UrlLocalizationTest(BaseTestCase):
    """localize url"""
    
    def setUp(self):
        self.user = None
        activate(settings.LANGUAGES[0][0])
    
    def tearDown(self):
        activate(settings.LANGUAGES[0][0])
    
    def _log_as_editor(self):
        """Log as editor"""
        self.user = user = User.objects.create_user('toto', 'toto@toto.fr', 'toto')
        
        content_type = ContentType.objects.get_for_model(get_article_class())
        
        perm = 'change_{0}'.format(content_type.model)
        can_edit_article = Permission.objects.get(content_type=content_type, codename=perm)
        user.user_permissions.add(can_edit_article)
        
        perm = 'add_{0}'.format(content_type.model)
        can_add_article = Permission.objects.get(content_type=content_type, codename=perm)
        user.user_permissions.add(can_add_article)
        
        user.is_active = True
        user.save()
        return self.client.login(username='toto', password='toto')
    
    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_get_locale_article(self):
        """get article with locale slug"""
        original_text = '*!-+' * 10
        translated_text = ':%@/' * 9
        
        art1 = get_article_class().objects.create(title="Home", content=original_text)
        
        origin_lang = settings.LANGUAGES[0][0]
        trans_lang = settings.LANGUAGES[1][0]
        
        setattr(art1, 'title_' + trans_lang, 'Accueil')
        setattr(art1, 'content_' + trans_lang, translated_text)
        art1.save()
        
        response = self.client.get('/{0}/home/'.format(origin_lang), follow=True)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, original_text)
        
        response = self.client.get('/{0}/accueil/'.format(trans_lang), follow=True)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, translated_text)

    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_change_lang(self):
        """change language"""

        original_text = u'*!-+' * 10
        translated_text = u':%@/' * 9
        
        art1 = get_article_class().objects.create(title="Home", content=original_text)
        
        origin_lang = settings.LANGUAGES[0][0]
        trans_lang = settings.LANGUAGES[1][0]

        activate(origin_lang)

        setattr(art1, 'title_' + trans_lang, u'Accueil')
        setattr(art1, 'content_' + trans_lang, translated_text)
        
        art1.save()
        
        origin_url = '/{0}/home/'.format(origin_lang)
        response = self.client.get(origin_url, follow=True)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, original_text)
        
        data = {'language': trans_lang}
        response = self.client.post(
            reverse('coop_cms_change_language') + '?next={0}'.format(origin_url),
            data=data,
            follow=True
        )
        self.assertEqual(200, response.status_code)
        self.assertContains(response, translated_text)
        
        response = self.client.get('/{0}/accueil/'.format(trans_lang), follow=True)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, translated_text)
        
    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_change_lang_next_url_after(self):
        """change language and redirect to url"""
        
        original_text = '*!-+' * 10
        translated_text = ':%@/' * 9
        
        art1 = get_article_class().objects.create(title="Home", content=original_text)
        
        art2 = get_article_class().objects.create(title="Next", content="****NEXT****")
        
        origin_lang = settings.LANGUAGES[0][0]
        trans_lang = settings.LANGUAGES[1][0]
        
        setattr(art1, 'title_' + trans_lang, 'Accueil')
        setattr(art1, 'content_' + trans_lang, translated_text)
        
        art1.save()
        
        origin_url = '/{0}/home/'.format(origin_lang)
        response = self.client.get(origin_url, follow=True)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, original_text)
        
        data = {'language': trans_lang, 'next_url_after_change_lang': art2.get_absolute_url()}
        response = self.client.post(
            reverse('coop_cms_change_language'),
            data=data,
            follow=True
        )
        self.assertEqual(200, response.status_code)
        self.assertContains(response, art2.content)
            
    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_change_lang_no_trans(self):
        """change language and no translation"""

        original_text = '*!-+' * 10
        
        get_article_class().objects.create(title="Home", content=original_text)
        
        origin_lang = settings.LANGUAGES[0][0]
        trans_lang = settings.LANGUAGES[1][0]
        
        origin_url = '/{0}/home/'.format(origin_lang)
        response = self.client.get(origin_url, follow=True)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, original_text)
        
        data = {'language': trans_lang}
        response = self.client.post(
            reverse('coop_cms_change_language') + '?next={0}'.format(origin_url),
            data=data,
            follow=True
        )
        self.assertEqual(200, response.status_code)
        self.assertContains(response, original_text)
        
        response = self.client.get('/{0}/home/'.format(trans_lang), follow=True)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, original_text)
            
    def test_keep_slug(self):
        """test slug are not modified when changing title"""
        article_class = get_article_class()
        art1 = article_class.objects.create(title=u"Home", content="aa")
        original_slug = art1.slug
        art1.title = "Title changed"
        art1.save()
        art1 = article_class.objects.get(id=art1.id)
        self.assertEqual(original_slug, art1.slug)
        
    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_keep_localized_slug(self):
        """test translation of slug are not modified when changing title"""
        
        article_class = get_article_class()
        art1 = article_class.objects.create(title=u"Home", content="aa")
        trans_lang = settings.LANGUAGES[1][0]
        setattr(art1, 'title_' + trans_lang, u'Accueil')
        art1.save()
        
        original_slug = art1.slug
        original_trans_slug = getattr(art1, 'slug_' + trans_lang, u'**dummy**')
        
        art1.title = u"Title changed"
        setattr(art1, 'title_' + trans_lang, u'Titre change')
        
        art1.save()
        art1 = article_class.objects.get(id=art1.id)
        
        self.assertEqual(original_slug, art1.slug)
        self.assertEqual(original_trans_slug, getattr(art1, 'slug_' + trans_lang))
        
    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_localized_slug_already_existing(self):
        """test localized slug already exists"""
        
        article_class = get_article_class()
        art1 = article_class.objects.create(title=u"Home", content="aa")
        art2 = article_class.objects.create(title=u"Rome", content="aa")

        trans_lang = settings.LANGUAGES[1][0]
        setattr(art1, 'title_' + trans_lang, art2.title)
        art1.save()
        
        art2.save()
        
        setattr(art2, 'title_' + trans_lang, art2.title)
        art2.save()
        
        self.assertNotEqual(getattr(art2, 'slug_' + trans_lang), getattr(art1, 'slug_' + trans_lang))
        
    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_localized_slug_already_existing2(self):
        """test localized slug already exists 2 """
        
        article_class = get_article_class()
        art1 = article_class.objects.create(title=u"Home", content="aa")
        art2 = article_class.objects.create(title=u"Rome", content="aa")

        trans_lang = settings.LANGUAGES[1][0]
        setattr(art1, 'title_' + trans_lang, art2.title)
        art1.save()
        
        setattr(art2, 'title_' + trans_lang, art2.title)
        art2.save()
        
        self.assertNotEqual(getattr(art2, 'slug_' + trans_lang), getattr(art1, 'slug_' + trans_lang))
        
    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_localized_slug_already_existing3(self):
        """test localized slug already exists 3 """
        self._log_as_editor()
        article_class = get_article_class()

        art1 = article_class.objects.create(title=u"Home", content="aa")
        art2 = article_class.objects.create(title=u"Rome", content="aa", template='test/article.html')

        trans_lang = settings.LANGUAGES[1][0]
        setattr(art1, 'title_' + trans_lang, art2.title)
        art1.save()
        
        # CHANGE LANGUAGE
        activate(trans_lang)
        
        url = art2.get_edit_url()
        
        data = {
            'title': art2.title,
            'content': 'translation', 
        }
        
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        art2_updated = article_class.objects.get(id=art2.id)
        
        self.assertEqual(getattr(art2_updated, 'title_' + trans_lang), art2.title)
        
        self.assertNotEqual(getattr(art2_updated, 'slug_' + trans_lang), getattr(art1, 'slug_' + trans_lang))
        
    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_localize_existing_article1(self):
        """test localized existing article 1 """

        self._log_as_editor()
        article_class = get_article_class()
        art1 = article_class.objects.create(title=u"Home", template='test/article.html')

        origin_lang = settings.LANGUAGES[0][0]
        trans_lang = settings.LANGUAGES[1][0]
        
        # CHANGE LANGUAGE
        activate(trans_lang)
        
        url = art1.get_edit_url()
        
        data = {
            'title': u"Home",
            'content': 'translation', 
        }
        
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        art1_updated = article_class.objects.get(id=art1.id)
        
        self.assertEqual(getattr(art1_updated, 'title_' + trans_lang), art1.title)
        self.assertEqual(getattr(art1_updated, 'slug_' + trans_lang), getattr(art1, 'slug_' + origin_lang))
        
    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_localize_existing_article2(self):
        """test localized existing article 2 """
        self._log_as_editor()
        article_class = get_article_class()
        art1 = article_class.objects.create(title=u"Accueil", template='test/article.html')

        origin_lang = settings.LANGUAGES[0][0]
        trans_lang = settings.LANGUAGES[1][0]
        
        # CHANGE LANGUAGE
        activate(trans_lang)
        
        url = art1.get_edit_url()
        
        data = {
            'title': u"Home",
            'content': 'translation', 
        }
        
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        art1_updated = article_class.objects.get(id=art1.id)
        self.assertEqual(getattr(art1_updated, 'title_' + origin_lang), art1.title)
        self.assertEqual(getattr(art1_updated, 'title_' + trans_lang), data["title"])
        self.assertEqual(getattr(art1_updated, 'slug_' + trans_lang), "home")
        self.assertEqual(getattr(art1_updated, 'slug_' + origin_lang), "accueil")
        
    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_localized_slug_already_existing4(self):
        """test localized slug and existing article """
        self._log_as_editor()
        article_class = get_article_class()
        art1 = article_class.objects.create(title=u"Home", content="aa")
        art2 = article_class.objects.create(title=u"Rome", content="aa", template='test/article.html')

        trans_lang = settings.LANGUAGES[1][0]
        
        self.assertEqual(None, getattr(art2, 'slug_' + trans_lang))
        
        # CHANGE LANGUAGE
        activate(trans_lang)
        
        url = art2.get_edit_url()
        
        data = {
            'title': art1.title,
            'content': 'translation', 
        }
        
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        art2_updated = article_class.objects.get(id=art2.id)
        
        self.assertEqual(getattr(art2_updated, 'title_' + trans_lang), art1.title)
        
        self.assertNotEqual(getattr(art2_updated, 'slug_' + trans_lang), art1.slug)
        
    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_localized_slug_already_existing5(self):
        """test localized slug existing and existing article """

        self._log_as_editor()
        article_class = get_article_class()
        art1 = article_class.objects.create(title=u"Home", content="aa")
        art2 = article_class.objects.create(title=u"Rome", content="aa", template='test/article.html')

        trans_lang = settings.LANGUAGES[1][0]
        
        self.assertEqual(None, getattr(art2, 'slug_' + trans_lang))
        
        setattr(art2, 'title_' + trans_lang, art1.title)
        art2.save()
        self.assertNotEqual(art1.slug, getattr(art2, 'slug_' + trans_lang))
        
        # CHANGE LANGUAGE
        activate(trans_lang)
        
        url = art2.get_edit_url()
        
        data = {
            'title': art1.title,
            'content': 'translation', 
        }
        
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        
        art2_updated = article_class.objects.get(id=art2.id)
        
        self.assertEqual(getattr(art2_updated, 'title_' + trans_lang), art1.title)
        
        self.assertNotEqual(getattr(art2_updated, 'slug_' + trans_lang), art1.slug)
            
    def test_no_title(self):
        """test create article without title"""
        article_class = get_article_class()
        
        try:
            article_class.objects.create(title=u"", content="a!*%:" * 10, publication=BaseArticle.PUBLISHED)
        except InvalidArticleError:
            # OK
            return

        # Force to fail
        self.assertFalse(True)

    @skipIf(not is_localized() or not is_multilang(), "not localized")
    @override_settings(MODELTRANSLATION_FALLBACK_LANGUAGES=language_fallbacks())
    def test_create_article_in_additional_lang_fallback(self):
        """test create article into an other language than the default"""

        article_class = get_article_class()
        
        default_lang = settings.LANGUAGES[0][0]
        other_lang = settings.LANGUAGES[1][0]
        
        activate(other_lang)
        
        art1 = article_class.objects.create(title=u"abcd", content="a!*%:" * 10, publication=BaseArticle.PUBLISHED)
        
        response = self.client.get(art1.get_absolute_url())
        self.assertEqual(200, response.status_code)
        self.assertContains(response, art1.content)
        
        activate(default_lang)
        
        response = self.client.get(art1.get_absolute_url())
        self.assertEqual(200, response.status_code)
        self.assertContains(response, art1.content)

    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_create_article_in_additional_lang_no_fallback(self):
        """test create article into an other language than the default"""

        article_class = get_article_class()

        default_lang = settings.LANGUAGES[0][0]
        other_lang = settings.LANGUAGES[1][0]

        activate(other_lang)

        art1 = article_class.objects.create(title=u"abcd", content="a!*%:" * 10, publication=BaseArticle.PUBLISHED)

        response = self.client.get(art1.get_absolute_url())
        self.assertEqual(200, response.status_code)
        self.assertContains(response, art1.content)

        activate(default_lang)

        response = self.client.get(art1.get_absolute_url())
        self.assertEqual(404, response.status_code)

    @skipIf(not is_localized() or multilang_mode() < 3, "not localized")
    def test_create_article_in_third_lang(self):
        """test create article into an other language than the default"""

        article_class = get_article_class()

        default_lang = settings.LANGUAGES[0][0]
        other_lang = settings.LANGUAGES[1][0]
        third_lang = settings.LANGUAGES[2][0]

        activate(third_lang)
        content = u"a!*%:"*10

        art1 = article_class.objects.create(title=u"abcd", content=content, publication=BaseArticle.PUBLISHED)
        self.assertEqual(art1.slug, 'abcd')
        third_lang_url = art1.get_absolute_url()
        response = self.client.get(third_lang_url)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, content)

        activate(other_lang)
        art1.title = 'efgh'
        art1.save()

        self.assertEqual(art1.slug, 'efgh')

        response = self.client.get(art1.get_absolute_url())
        self.assertEqual(200, response.status_code)
        self.assertNotContains(response, content)

        response = self.client.get(third_lang_url.replace('/' + third_lang + '/', '/' + other_lang + '/', 1))
        self.assertEqual(404, response.status_code)

    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_redirect_to_language(self):
        """check redirect_to_language utility"""
        article_class = get_article_class()

        other_lang = settings.LANGUAGES[1][0]

        art1 = article_class.objects.create(title=u"abcd", publication=BaseArticle.PUBLISHED)

        response = redirect_to_language(art1.get_absolute_url(), other_lang)

        self.assertTrue(response.url.find("/" + other_lang + "/") == 0)
        self.assertEqual(get_language(), other_lang)

    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_redirect_to_invalid_language(self):
        """check redirect_to_language uitiliy raise error if ImproperlyConfigured"""

        article_class = get_article_class()

        art1 = article_class.objects.create(title=u"abcd", publication=BaseArticle.PUBLISHED)

        self.assertRaises(ImproperlyConfigured, redirect_to_language, art1.get_absolute_url(), "zz")


class SwitchLanguageTest(BaseTestCase):
    """change the language from coop-bar popup"""

    def setUp(self):
        self.user = None
        activate(settings.LANGUAGES[0][0])

    def tearDown(self):
        activate(settings.LANGUAGES[0][0])

    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_get_language_switcher(self):
        """get article with locale slug"""

        original_text = '*!-+' * 10
        translated_text = ':%@/' * 9

        art1 = get_article_class().objects.create(title="Home", content=original_text)

        origin_lang = settings.LANGUAGES[0][0]
        trans_lang = settings.LANGUAGES[1][0]

        setattr(art1, 'title_' + trans_lang, 'Accueil')
        setattr(art1, 'content_' + trans_lang, translated_text)
        art1.save()

        url = reverse('coop_cms_switch_language_popup')

        response = self.client.get(url)
        soup = BeautifulSoup(response.content)
        self.assertEqual(len(soup.select('select#id_language option')), len(settings.LANGUAGES))

    @skipIf(not is_localized() or not is_multilang(), "not localized")
    def test_change_lang(self):
        """change language"""

        original_text = u'*!-+' * 10
        translated_text = u':%@/' * 9

        art1 = get_article_class().objects.create(title="Home", content=original_text)

        origin_lang = settings.LANGUAGES[0][0]
        trans_lang = settings.LANGUAGES[1][0]

        activate(origin_lang)

        setattr(art1, 'title_' + trans_lang, u'Accueil')
        setattr(art1, 'content_' + trans_lang, translated_text)

        art1.save()

        data = {'language': trans_lang}
        response = self.client.post(
            reverse('coop_cms_switch_language_popup'),
            data=data,
            follow=True
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(trans_lang, get_language())

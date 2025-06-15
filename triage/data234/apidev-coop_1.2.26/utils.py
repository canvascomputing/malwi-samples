# -*- coding: utf-8 -*-
"""utils"""

from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from threading import current_thread
from traceback import print_exc

from slugify import slugify as unicode_slugify

from django import VERSION
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import get_connection, EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse, NoReverseMatch
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.utils import translation
from django.utils.text import slugify as ascii_slugify

from coop_cms.settings import get_newsletter_context_callbacks, get_eastern_languages


if VERSION >= (1, 9, 0):
    from wsgiref.util import FileWrapper
else:
    from django.core.servers.basehttp import FileWrapper
FileWrapper = FileWrapper


class _DeHTMLParser(HTMLParser):
    """html to text parser"""
    def __init__(self, allow_spaces=False, allow_html_chars=False):
        HTMLParser.__init__(self)
        self._text = []
        self._allow_spaces = allow_spaces
        self._allow_html_chars = allow_html_chars

    def handle_data(self, data):
        """parser"""
        text = data
        if not self._allow_spaces:
            text = sub('[ \t\r\n]+', u' ', text)
        self._text.append(text)

    def handle_entityref(self, name):
        html_char = u'&' + name + u";"
        if self._allow_html_chars:
            value = html_char
        else:
            value = self.unescape(html_char).replace(u'\xa0', u' ')
        self._text.append(value)

    def handle_charref(self, name):
        self.handle_entityref(u"#" + name)

    def handle_starttag(self, tag, attrs):
        """parser"""
        if tag == u'p':
            self._text.append('\n\n')
        elif tag == u'br':
            self._text.append('\n')

    def handle_startendtag(self, tag, attrs):
        """parser"""
        if tag == u'br':
            self._text.append('\n\n')

    def text(self):
        """parser"""
        return u''.join(self._text).strip()


def dehtml(text, allow_spaces=False, allow_html_chars=False):
    """
    html to text
    copied from http://stackoverflow.com/a/3987802/117092
    """
    try:
        parser = _DeHTMLParser(allow_spaces=allow_spaces, allow_html_chars=allow_html_chars)
        parser.feed(text)
        parser.close()
        return parser.text()
    except Exception:  # pylint: disable=broad-except
        print_exc(file=stderr)
        return text


def strip_a_tags(pretty_html_text):
    """
    Reformat prettified html to remove spaces in <a> tags
    """
    pos = 0
    fixed_html = u''
    while True:
        new_pos = pretty_html_text.find('<a', pos)
        if new_pos > 0:
            fixed_html += pretty_html_text[pos:new_pos]
            end_tag = pretty_html_text.find('>', new_pos + 1)
            end_pos = pretty_html_text.find('</a>', end_tag + 1)

            fixed_html += pretty_html_text[new_pos:end_tag + 1]
            tag_content = pretty_html_text[end_tag + 1:end_pos]
            fixed_html += tag_content.strip() + '</a>'

            pos = end_pos + 4
        else:
            fixed_html += pretty_html_text[pos:]
            break

    return fixed_html


def _replace_from_end(s, a, b, times=None):
    """replace from end"""
    return s[::-1].replace(a, b, times)[::-1]


def avoid_line_too_long(pretty_html_text):
    """
    detect any line with more than 998 characters
    """
    lines = pretty_html_text.split(u'\n')
    new_lines = []
    for line in lines:
        line_length = len(line)
        if line_length >= 998:
            # Cut the line in several parts of 900 characters
            parts = []
            part_size = 900
            part_index = 0
            while part_size * len(parts) < line_length:
                parts.append(line[part_index*part_size:(part_index + 1)*part_size])
                part_index = len(parts)
            parts = [_replace_from_end(part, u' ', u'\n', 1) for part in parts]
            new_lines.append(u''.join(parts))
        else:
            new_lines.append(line)
    return u'\n'.join(new_lines)


def make_links_absolute(html_content, newsletter=None, site_prefix=""):
    """replace all local url with site_prefixed url"""
    
    def make_abs(url):
        """make absolute url"""
        if url.startswith('..'):
            url = url[2:]
        while url.startswith('/..'):
            url = url[3:]
        if url.startswith('/'):
            url = '%s%s' % (site_prefix, url)
        return url

    if not site_prefix:
        site_prefix = newsletter.get_site_prefix() if newsletter else settings.COOP_CMS_SITE_PREFIX

    soup = BeautifulSoup(html_content, 'html.parser')
    for a_tag in soup.find_all("a"):
        if a_tag.get("href", None):
            a_tag["href"] = make_abs(a_tag["href"])
    
    for img_tag in soup.find_all("img"):
        if img_tag.get("src", None):
            img_tag["src"] = make_abs(img_tag["src"])

    pretty_html = soup.prettify()
    fixed_html = strip_a_tags(pretty_html)
    return avoid_line_too_long(fixed_html)


def _send_email(subject, html_text, dests, list_unsubscribe):
    """send an email"""
    emails = []
    connection = get_connection()
    from_email = getattr(settings, 'COOP_CMS_FROM_EMAIL', settings.DEFAULT_FROM_EMAIL)
    reply_to = getattr(settings, 'COOP_CMS_REPLY_TO', None)

    # make header
    headers = {}
    if reply_to:
        headers['Reply-To'] = reply_to
    if list_unsubscribe:
        headers['List-Unsubscribe'] = ", ".join(["<{0}>".format(url) for url in list_unsubscribe])

    for address in dests:
        text = dehtml(html_text)
        email = EmailMultiAlternatives(subject, text, from_email, [address], headers=headers)
        email.attach_alternative(html_text, "text/html")
        emails.append(email)
    return connection.send_messages(emails)


def _activate_lang(lang=None):
    lang = lang or get_language()
    language_codes = [code_and_name[0] for code_and_name in settings.LANGUAGES]
    if not (lang in language_codes):
        # The current language is not defined in settings.LANGUAGE
        # force it to the defined language
        lang = settings.LANGUAGE_CODE[:2]
    translation.activate(lang)


def send_email(subject, template_name, context, site_prefix, dests, lang=None, list_unsubscribe=None):
    """Send an HTML email"""
    _activate_lang(lang)

    the_template = get_template(template_name)

    try:
        html_text = the_template.render(context)
    except Exception:
        # import traceback
        # print traceback.print_exc()
        raise

    html_text = make_links_absolute(html_text, site_prefix=site_prefix)

    return _send_email(subject, html_text, dests, list_unsubscribe=list_unsubscribe)


def get_language():
    """returns the language or default language"""
    lang = translation.get_language()
    if lang:
        return lang[:2]
    else:
        return settings.LANGUAGE_CODE[:2]


def send_newsletter(newsletter, dests, list_unsubscribe=None):
    """
    send newsletter
    newsletter : a newsletter object
    dests : the list of recipients
    list_unsubscribe : a list of url for unsubscribe
    """

    # Force the newsletter as public
    newsletter.is_public = True
    newsletter.save()

    lang = get_language()
    if not (lang in [code_and_name[0] for code_and_name in settings.LANGUAGES]):
        # The current language is not defined in settings.LANGUAGE
        # force it to the defined language
        lang = settings.LANGUAGE_CODE[:2]
        translation.activate(lang)

    the_template = get_template(newsletter.get_template_name())
    context_dict = {
        'title': newsletter.subject,
        'newsletter': newsletter,
        'by_email': True,
        'SITE_PREFIX': settings.COOP_CMS_SITE_PREFIX,
        'MEDIA_URL': settings.MEDIA_URL,
        'STATIC_URL': settings.STATIC_URL,
    }

    for callback in get_newsletter_context_callbacks():
        data = callback(newsletter)
        if data:
            context_dict.update(data)

    try:
        html_text = the_template.render(context_dict)
    except Exception:
        # import traceback
        # print traceback.print_exc()
        raise

    html_text = make_links_absolute(html_text, newsletter)

    return _send_email(newsletter.subject, html_text, dests, list_unsubscribe)


class RequestNotFound(Exception):
    """exception"""
    pass


class RequestManager(object):
    """get django request from anywhere"""
    _shared = {}

    def __init__(self):
        """his is a Borg"""
        self.__dict__ = RequestManager._shared
        
    def _get_request_dict(self):
        """request dict"""
        if not hasattr(self, '_request'):
            self._request = {}  # pylint: disable=attribute-defined-outside-init
        return self._request
    
    def clean(self):
        """clean"""
        if hasattr(self, '_request'):
            del self._request
        
    def get_request(self):
        """return request"""
        _requests = self._get_request_dict()
        the_thread = current_thread()
        if the_thread not in _requests:
            raise RequestNotFound("Request not found: make sure that middleware is installed")
        return _requests[the_thread]
    
    def set_request(self, request):
        """set request"""
        _requests = self._get_request_dict()
        _requests[current_thread()] = request


class RequestMiddleware(object):
    """middleware for request"""

    def process_request(self, request):
        """middleware is called before every request"""
        RequestManager().set_request(request)


def get_url_in_language(url, lang_code):
    """returns the url in another language"""
    if lang_code and translation.check_for_language(lang_code):
        path = strip_locale_path(url)[1]
        new_url = make_locale_path(path, lang_code)
        return new_url
    else:
        raise ImproperlyConfigured("{0} is not a valid language".format(lang_code))


def strip_locale_path(locale_path):
    """returns language independent url - /en/home/ --> /home/"""
    elements = locale_path.split('/')
    if len(elements) > 2:
        lang = elements[1]
        if lang in [lang_and_name[0] for lang_and_name in settings.LANGUAGES]:
            del elements[1]
            return lang, '/'.join(elements)
    return '', locale_path


def make_locale_path(path, lang):
    """returns locale url - /home/ --> /en/home/"""
    return u'/{0}{1}'.format(lang, path)


def redirect_to_language(url, lang_code):
    """change the language"""
    new_url = get_url_in_language(url, lang_code)
    translation.activate(lang_code)
    return HttpResponseRedirect(new_url)


def get_model_name(model_class):
    """return model name"""
    meta_class = getattr(model_class, '_meta')
    return getattr(meta_class, 'module_name', '') or getattr(meta_class, 'model_name')


def get_model_label(model_class):
    """return model name"""
    meta_class = getattr(model_class, '_meta')
    return getattr(meta_class, 'verbose_name')


def get_model_app(model_class):
    """return app name for this model"""
    meta_class = getattr(model_class, '_meta')
    return getattr(meta_class, 'app_label')


def get_text_from_template(template_name, extra_context=None):
    """
    load a template and render it as text
    :parameter template_name: the path to a template
    :parameter extra_context: some context for rendering
    :return text
    """
    context = extra_context or {}
    template = get_template(template_name)
    return template.render(context)


def paginate(request, queryset, items_count):
    try:
        page = int(request.GET.get('page', 0) or 0)
    except ValueError:
        page = 1
    paginator = Paginator(queryset, items_count)
    try:
        page_obj = paginator.page(page or 1)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


def get_login_url():
    """returns the URL of the login page"""
    try:
        return reverse("auth_login")
    except NoReverseMatch:
        return reverse("login")


def slugify(text, lang=None):
    """
    slugify a text. Use different method according to language
    "Here COmme the Sun" --> "here-come-the-sun"
    "Voici l'été" --> "voici-l-ete"
    "Миниаль бом" --> "Миниаль-бом"
    Args:
        text: a text to turn into a slug
        lang: the language of this text
    Returns: a slug
    """
    if lang is None:
        lang = get_language()

    if lang in get_eastern_languages():
        return unicode_slugify(text)
    else:
        return ascii_slugify(text)

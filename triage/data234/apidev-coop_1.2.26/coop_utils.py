# -*- coding: utf-8 -*-
"""
misc. templatetags
"""

import os.path
import time
import unicodedata

from bs4 import BeautifulSoup
from HTMLParser import HTMLParseError

from django import template
from django.conf import settings
from django.template import RequestContext
from django.template.base import TemplateSyntaxError
from django.template.loader import get_template
from django.utils.safestring import mark_safe

from floppyforms import CheckboxInput

from coop_cms.models import ArticleCategory, Image, Document
from coop_cms.settings import get_article_class, logger
from coop_cms.shortcuts import get_article
from coop_cms.utils import dehtml as do_dehtml, slugify

register = template.Library()


class ArticleLinkNode(template.Node):
    """create an article and returns a link into template"""

    def __init__(self, title, lang):
        self.title = title
        self.lang = lang

    def get_language(self, context):
        """get language from context"""
        request = context.get('request', None)
        lang = "en"
        if request:
            lang = getattr(request, 'LANGUAGE_CODE', lang)
        elif hasattr(settings, 'LANGUAGES'):
            lang = settings.LANGUAGES[0][0]
        elif hasattr(settings, 'LANGUAGE_CODE'):
            lang = settings.LANGUAGE_CODE[:2]
        return lang

    def render(self, context):
        """to html"""
        article_class = get_article_class()
        
        try:
            variable = template.Variable(self.title)
            title = variable.resolve(context)
        except template.VariableDoesNotExist:
            title = self.title.strip("'").strip('"')
        
        slug = slugify(title)
        try:
            if self.lang:
                article = get_article(slug, force_lang=self.lang)
            else:
                # If the language is not defined, we need to get it from the context
                # The Django get_language api doesn't work in template-tag
                article = get_article(slug, current_lang=self.get_language(context))
        except article_class.DoesNotExist:
            try:
                article = get_article(slug, all_langs=True)
            except article_class.DoesNotExist:
                article = article_class.objects.create(slug=slug, title=title)
        return article.get_absolute_url()


@register.tag
def article_link(parser, token):
    """template tag"""
    args = token.split_contents()
    title = args[1]
    lang = args[2] if len(args) > 2 else None
    return ArticleLinkNode(title, lang)


@register.filter
def dehtml(value):
    """
    html to text : Remove all tags
    <p>Hello&nbsp;World<p> --> Hello World
    """
    return do_dehtml(value)


@register.filter
def detagiffy(value):
    """
    html to text: Remove tags but keep html chars
    <p>Hello&nbsp;World<p> --> Hello&nbsp;World
    """
    return mark_safe(do_dehtml(value, allow_html_chars=True))

@register.filter
def sp_rt_lb(value):
    """clean"""
    return value.replace("\n", " ").replace("\r", "")


class NewsletterFriendlyCssNode(template.Node):
    """css in tags attributes"""
    def __init__(self, nodelist_content, css, css_order):
        self.css = css
        self.css_order = css_order
        self.nodelist_content = nodelist_content

    def _style_to_dict(self, style):
        """
        convert a style string ('color: #fff; background: #000') into a dict {'color': ''#fff', 'background': '#000'}
        """
        css_values = [elt for elt in style.strip().split(";") if elt]
        css_values = [elt.split(":") for elt in css_values]
        return dict([(key.strip(), value.strip()) for (key, value) in css_values])

    def _style_to_list(self, style):
        """
        convert a style string ('color: #fff; background: #000') into a list ['color', 'background']
        """
        css_values = [elt for elt in style.strip().split(";") if elt]
        css_values = [elt.split(":") for elt in css_values]
        return [key_and_value[0].strip() for key_and_value in css_values]

    def _dict_to_style(self, style_dict, order_of_items):
        """
        convert a dict {'color': ''#fff', 'background': '#000'} into a style string ('color: #fff; background: #000')
        """
        values = []
        for elt in order_of_items:
            value = style_dict.pop(elt, '')
            if value:
                values.append(u"{0}: {1}".format(elt, value))
        values.extend([u"{0}: {1}".format(key, value) for (key, value) in style_dict.items()])
        if values:
            return u"; ".join(values) + ";"
        return u""

    def render(self, context):
        """to html"""
        content = self.nodelist_content.render(context)
        if context.get('by_email', False):
            # avoid string.format issues with curly brackets
            try:
                soup = BeautifulSoup(content, "html.parser")
            except HTMLParseError as msg:
                logger.error("HTMLParseError: %s", msg)
                logger.error(content)
                raise

            for tag in self.css_order:
                css = self.css[tag]
                key_and_values = self._style_to_dict(css)
                key_order = self._style_to_list(css)
                for html_tag in soup.select(tag):
                    try:
                        # do not overwrite an inline css value
                        style = html_tag["style"]
                        style_list = self._style_to_list(style)
                        style_dict = self._style_to_dict(style)
                    except KeyError:
                        style_dict = {}
                        style_list = key_order
                    for key in key_order:
                        if key not in style_dict:
                            value = key_and_values[key]
                            style_dict[key] = value
                    # keep items in order
                    html_tag["style"] = self._dict_to_style(style_dict, style_list)

            # Do not prettify : it may cause some display problems
            content = unicode(soup)  # .prettify(formatter="minimal")

        else:
            style = ""
            for tag in reversed(self.css.keys()):
                value = self.css[tag]
                style += u"{0} {{ {1} }}\n".format(tag, value)
            content = u"<style>\n{0}</style>\n".format(style) + content
        return content


@register.tag
def nlf_css(parser, token):
    """Newsletter friendly CSS"""
    args = token.split_contents()
    css = {}
    css_order = []
    for item in args[1:]:
        tag, value = item.split("=")
        tag, value = tag.strip('"'), value.strip('"')
        css[tag] = value
        css_order.append(tag)
    nodelist = parser.parse(('end_nlf_css',))
    token = parser.next_token()
    return NewsletterFriendlyCssNode(nodelist, css, css_order)


@register.filter
def normalize_utf8_to_ascii(ustr):
    """utf to ascii"""
    try:
        return unicodedata.normalize('NFKD', ustr).encode('ascii', 'ignore')
    except TypeError:
        return ustr
    

@register.filter(name='is_checkbox')
def is_checkbox(field):
    """is checkbox"""
    field = getattr(field, 'field', field) # get the field attribute of the field or the field itself
    if hasattr(field, 'widget'):
        return field.widget.__class__.__name__ == CheckboxInput().__class__.__name__
    return False


@register.filter
def index(seq, index_val):
    """get index"""
    try:
        return seq[index_val]
    except IndexError:
        return None


class CoopCategoryNode(template.Node):
    """get category in template context"""
    def __init__(self, cat_slug, var_name):
        self.category = None
        cat = cat_slug.strip("'").strip('"')
        self.cat_var, self.cat = None, None
        if cat_slug == cat:
            self.cat_var = template.Variable(cat)
        else:
            self.cat = cat
        self.var_name = var_name

    def render(self, context):
        """to html"""
        if self.cat_var:
            self.cat = self.cat_var.resolve(context)
        try:
            slug = slugify(self.cat)
            self.category = ArticleCategory.objects.get(slug=slug)
        except ArticleCategory.DoesNotExist:
            self.category = ArticleCategory.objects.create(name=self.cat)
        context.dicts[0][self.var_name] = self.category
        return ""


@register.tag
def coop_category(parser, token):
    """get category in template context"""
    args = token.split_contents()
    cat_slug = args[1]
    var_name = args[2]
    return CoopCategoryNode(cat_slug, var_name)


@register.filter
def basename(fullname):
    """os.path.basename"""
    return os.path.basename(fullname)


@register.filter
def get_parts(list_of_objs, number_of_parts):
    """slice"""
    nb_objs = len(list_of_objs)
    nb_by_part, extra_nb = nb_objs / number_of_parts, nb_objs % number_of_parts
    parts = []
    stop_index = 0
    for which_part in range(number_of_parts):
        start_index = 0 if (stop_index == 0) else (stop_index)
        stop_index = start_index + nb_by_part + (1 if (which_part < extra_nb) else 0)
        parts.append(list_of_objs[start_index:stop_index])
    return parts


@register.filter
def get_part(list_of_objs, partionning):
    """slices"""
    which_part, number_of_parts = [int(x) for x in partionning.split("/")]
    parts = get_parts(list_of_objs, number_of_parts)
    return parts[which_part-1]


@register.filter
def group_in_sublists(list_of_objs, subslist_size):
    """group_in_sublists([1, 2, 3, 4], 2) --> [[1, 2], [3, 4]]"""
    return [list_of_objs[i:i+subslist_size] for i in range(0, len(list_of_objs), subslist_size)]


class MediaListNode(template.Node):
    def __init__(self, model_class, filter_name, var_name):
        self.model_class = model_class
        stripped_filter_name = filter_name.strip("'").strip('"')
        self.filter_var, self.filter_value = None, None
        if stripped_filter_name == filter_name:
            self.filter_var = template.Variable(filter_name)
        else:
            self.filter_value = stripped_filter_name
        self.var_name = var_name

    def render(self, context):
        if self.filter_var:
            self.filter_value = self.filter_var.resolve(context)
        images = self.model_class.objects.filter(filters__name=self.filter_value).order_by("ordering", "-created")
        context.dicts[0][self.var_name] = images
        return ""


@register.tag
def coop_image_list(parser, token):
    """image list"""
    args = token.split_contents()
    try:
        filter_name = args[1]
        # as_name = args[2]
        var_name = args[3]
    except IndexError:
        raise TemplateSyntaxError(u"coop_image_list: usage --> {% coop_image_list 'filter_name' as var_name %}")
    return MediaListNode(Image, filter_name, var_name)


DEFAULT_ACCEPT_COOKIE_MESSAGE_TEMPLATE = 'coop_cms/_accept_cookies_message.html'


class ShowAcceptCookieMessageNode(template.Node):
    """accept cookie message"""
    def __init__(self, template_name):
        self.template_name = template_name or DEFAULT_ACCEPT_COOKIE_MESSAGE_TEMPLATE
        super(ShowAcceptCookieMessageNode, self).__init__()

    def render(self, context):
        """to html"""
        request = context.get('request', None)
        if not request.session.get('hide_accept_cookie_message', False):
            template_ = get_template(self.template_name)
            return template_.render(RequestContext(request, {}))
        else:
            return ""


@register.tag
def show_accept_cookie_message(parser, token):
    """show accept cookie message"""
    args = token.split_contents()
    if len(args) > 1:
        template_name = args[1].strip('"').strip('"')
    else:
        template_name = ""
    return ShowAcceptCookieMessageNode(template_name)


@register.filter
def open_tag_if(index_, args):
    """open_tag if condition"""
    tag, nb_per_block = args.split("/")
    nb_per_block = int(nb_per_block)
    return mark_safe(u"<{0}>".format(tag) if (index_ % nb_per_block) == 0 else "")


@register.filter
def close_tag_if(index_, args):
    """close_tag if condition"""
    tag, nb_per_block = args.split("/")
    nb_per_block = int(nb_per_block)
    return mark_safe(u"</{0}>".format(tag) if (index_ % nb_per_block) == nb_per_block else "")


@register.filter
def find_css(value, css_class):
    """open_tag if condition"""
    if css_class in value.split(" "):
        return True
    return False


class VersionedStaticFileNode(template.Node):
    """return static path with ?v=dateoflastchange"""
    def __init__(self, static_path):
        self.static_path = static_path.strip("'").strip('"')
        self.is_string = self.static_path == static_path

    def render(self, context):
        if settings.DEBUG:
            version = time.time()
        else:
            static_file_path = os.path.join(settings.STATIC_ROOT, self.static_path)
            try:
                #last Modification of the file
                version = os.path.getmtime(static_file_path)
            except OSError:
                version = 'x'
        return u"{0}{1}?v={2}".format(settings.STATIC_URL, self.static_path, version)


@register.tag
def versioned_static_file(parser, token):
    """image list"""
    args = token.split_contents()
    try:
        static_path = args[1]
    except IndexError:
        raise TemplateSyntaxError(u"coop_image_list: usage --> {% versioned_static_file 'static_path' %}")
    return VersionedStaticFileNode(static_path)


@register.tag
def coop_docs_list(parser, token):
    """image list"""
    args = token.split_contents()
    try:
        filter_name = args[1]
        # as_name = args[2]
        var_name = args[3]
    except IndexError:
        raise TemplateSyntaxError(u"coop_docs_list: usage --> {% coop_docs_list 'filter_name' as var_name %}")
    return MediaListNode(Document, filter_name, var_name)


@register.filter
def reduced_page_range(page_obj, max_num=10):
    nb_pages = len(page_obj.paginator.page_range)

    if nb_pages > max_num:
        current_page = page_obj.number

        start_value = max(1, current_page - 2)
        pages = list(range(start_value, current_page))

        pages += [current_page]

        end_value = min(nb_pages, current_page + 2)
        pages += list(range(current_page + 1, end_value + 1))

        if 1 not in pages:
            # If not in the list add first page
            extra_pages = [1, ]
            if pages[0] != 2:
                # Add separator if there is a gap between numbers
                extra_pages += [0, ]
            pages = extra_pages + pages

        if nb_pages not in pages:
            # If not in the list add separator and last page
            extra_pages = [nb_pages, ]
            if pages[-1] != nb_pages - 1:
                extra_pages = [0, ] + extra_pages
            pages += extra_pages

        return pages
    else:
        return page_obj.paginator.page_range


@register.filter
def unicode_slugify(value):
    """open_tag if condition"""
    return slugify(value)
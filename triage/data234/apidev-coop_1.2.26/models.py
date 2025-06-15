# -*- coding: utf-8 -*-
"""models"""

from datetime import datetime
import os
import os.path
import re
import shutil
import urlparse

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.contrib.staticfiles import finders
from django.core.exceptions import ValidationError
from django.core.files import File
from django.core.urlresolvers import reverse, NoReverseMatch
from django.db import models
from django.db.models import Q
from django.db.models.aggregates import Max
from django.db.models.signals import pre_delete, post_save
from django.template import RequestContext, Context
from django.template.loader import get_template
from django.utils.translation import get_language, ugettext, ugettext_lazy as _
from django.utils.html import escape

from django_extensions.db.models import TimeStampedModel, AutoSlugField
from sorl.thumbnail import default as sorl_thumbnail, delete as sorl_delete
from sorl.thumbnail.parsers import ThumbnailParseError

from coop_cms.settings import (
    get_article_class, get_article_logo_size, get_article_logo_crop, get_article_templates, get_default_logo,
    get_headline_image_size, get_headline_image_crop, get_img_folder, get_newsletter_item_classes,
    get_navtree_class, get_max_image_width, is_localized, is_requestprovider_installed, COOP_CMS_NAVTREE_CLASS,
    cms_no_homepage, homepage_no_redirection
)
from coop_cms.utils import dehtml, RequestManager, RequestNotFound, get_model_label, make_locale_path, slugify

ADMIN_THUMBS_SIZE = '60x60'


class InvalidArticleError(Exception):
    """The exception can be raised when article is not valid"""
    pass



def validate_slug(value):
    """check a slug only contains letters, numbers or hyphens (undercores are allowed)"""
    if not re.match(r"^[-\w]+$", value):
        raise ValidationError(_('The slug must only contains letters, numbers or hyphens'), code='invalid')


def get_object_label(content_type, obj):
    """
    returns the label used in navigation according to the configured rule
    """
    if not obj:
        return ugettext(u"Node")
    try:
        nav_type = NavType.objects.get(content_type=content_type)
        if nav_type.label_rule == NavType.LABEL_USE_SEARCH_FIELD:
            label = getattr(obj, nav_type.search_field)
        elif nav_type.label_rule == NavType.LABEL_USE_GET_LABEL:
            label = obj.get_label()
        else:
            label = u'{0}'.format(obj)
    except NavType.DoesNotExist:
        label = u'{0}'.format(obj)
    return label


def set_node_ordering(node, tree, parent):
    """change node ordering"""
    if parent:
        node.parent = parent
        sibling_nodes = NavNode.objects.filter(tree=tree, parent=node.parent)
    else:
        node.parent = None
        sibling_nodes = NavNode.objects.filter(tree=tree, parent__isnull=True)
    max_ordering = sibling_nodes.aggregate(max_ordering=Max('ordering'))['max_ordering'] or 0
    node.ordering = max_ordering + 1


def create_navigation_node(content_type, obj, tree, parent):
    """create navigation node"""
    node = NavNode(tree=tree, label=get_object_label(content_type, obj))
    # add it as last child of the selected node
    set_node_ordering(node, tree, parent)
    # associate with a content object
    node.content_type = content_type
    node.object_id = obj.id if obj else 0
    node.save()
    return node


def get_navigable_type_choices():
    """returns the list of choice of navigable types"""
    types = [('', '')]
    types += [
        (nav_type.content_type.id, u'{0}'.format(nav_type.content_type))
        for nav_type in NavType.objects.all()
    ]
    return types


class NavType(models.Model):
    """Define which ContentTypes can be inserted in the tree as content"""

    LABEL_USE_UNICODE = 0
    LABEL_USE_SEARCH_FIELD = 1
    LABEL_USE_GET_LABEL = 2

    LABEL_RULE_CHOICES = (
        (LABEL_USE_UNICODE, _(u'Use object unicode')),
        (LABEL_USE_SEARCH_FIELD, _(u'Use search field')),
        (LABEL_USE_GET_LABEL, _(u'Use get_label')),
    )

    content_type = models.OneToOneField(ContentType, verbose_name=_(u'django model'))
    search_field = models.CharField(max_length=200, blank=True, default="", verbose_name=_(u'search field'))
    label_rule = models.IntegerField(
        verbose_name=_(u'How to generate the label'), choices=LABEL_RULE_CHOICES, default=LABEL_USE_UNICODE
    )

    def __unicode__(self):
        return self.content_type.app_label+'.'+self.content_type.model

    class Meta:
        verbose_name = _(u'navigable type')
        verbose_name_plural = _(u'navigable types')


class BaseNavTree(models.Model):
    """Base class for nabigation tree. It is deprecated (not recommended) to use your own"""
    last_update = models.DateTimeField(auto_now=True)
    name = models.CharField(_(u'name'), max_length=100, db_index=True, unique=True, default='default')
    types = models.ManyToManyField('coop_cms.NavType', blank=True, related_name="%(app_label)s_%(class)s_set")

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        """url"""
        return reverse('navigation_tree', args=[self.id])

    def get_root_nodes(self):
        """nodes with no parents"""
        return NavNode.objects.filter(tree=self, parent__isnull=True).order_by("ordering")

    def get_root_nodes_count(self):
        """number of nodes without parents"""
        return self.get_root_nodes().count()
    get_root_nodes_count.short_description = _(u'root nodes')

    class Meta:
        verbose_name = _(u'Navigation tree')
        verbose_name_plural = _(u'Navigation trees')
        abstract = True


class NavTree(BaseNavTree):
    """Implementation of NavTree: Use this one. Don't create your own"""

    def __unicode__(self):
        return self.name


class NavNode(models.Model):
    """
    A navigation node
    Part of the tree as child of his parent
    Point on a content_object
    """

    tree = models.ForeignKey(COOP_CMS_NAVTREE_CLASS, verbose_name=_("tree"))
    label = models.CharField(max_length=200, verbose_name=_("label"))
    parent = models.ForeignKey("NavNode", blank=True, null=True, default=0, verbose_name=_("parent"))
    ordering = models.PositiveIntegerField(_("ordering"), default=0)

    # generic relation
    content_type = models.ForeignKey(ContentType, verbose_name=_("content_type"), blank=True, null=True)
    object_id = models.PositiveIntegerField(verbose_name=_("object id"), blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    in_navigation = models.BooleanField(_("in navigation"), default=True)

    def get_absolute_url(self):
        """url"""
        try:
            if self.content_object:
                return self.content_object.get_absolute_url()
        except AttributeError:
            pass
        return None
    
    def is_active_node(self):
        """true if link correspond to the current page"""
        url = self.get_absolute_url()
        if url and is_requestprovider_installed():
            try:
                http_request = RequestManager().get_request()
                return http_request and http_request.path == url
            except RequestNotFound:
                pass
        return False

    def get_content_name(self):
        """friendly name of the object model"""
        return get_model_label(self.content_type.model_class())

    def __unicode__(self):
        if self.parent:
            return u'{0} > {1}'.format(self.parent, self.label)
        return self.label

    class Meta:
        verbose_name = _(u'navigation node')
        verbose_name_plural = _(u'navigation nodes')

    def is_accessible(self):
        """returns True if the content can be accessed"""

        # If I point to a content : returns True if content can be accesssed
        if self.content_object:
            is_accessible_method = getattr(self.content_object, 'is_accessible', None)
            if callable(is_accessible_method):
                return is_accessible_method()
            else:
                if is_accessible_method is None:
                    return True
                else:
                    return is_accessible_method

        # returns True if I have children which can be accessed
        for child in self.get_children(in_navigation=True):
            if child.is_accessible():
                return True

        return False

    def get_children(self, in_navigation=None, allow_all=False):
        """children of the node"""
        nodes = NavNode.objects.filter(parent=self).order_by("ordering")
        # Be careful : in_navigation can be False
        if in_navigation is not None:
            nodes = nodes.filter(in_navigation=in_navigation)

        if not allow_all:
            exclude_ids = []
            for node in nodes:
                if not node.is_accessible():
                    exclude_ids.append(node.id)
            if exclude_ids:
                nodes = nodes.exclude(id__in=exclude_ids)

        return nodes

    def has_children(self):
        """True if has children"""
        return self.get_children(True).count()
    
    def get_children_count(self):
        """number of children"""
        return self.get_children(True).count()
    
    def get_children_navigation(self):
        """children"""
        return self.get_children(True)

    def get_siblings(self, in_navigation=None):
        """other nodes at same level"""
        nodes = NavNode.objects.filter(parent=self.parent).order_by("ordering")
        if in_navigation is not None:
            nodes = nodes.filter(in_navigation=in_navigation)

        exclude_ids = []
        for node in nodes:
            if not node.is_accessible():
                exclude_ids.append(node.id)
        if exclude_ids:
            nodes = nodes.exclude(id__in=exclude_ids)

        return nodes

    def get_progeny(self, level=0):
        """children, grand-children ..."""
        progeny = [(self, level)]
        for child in NavNode.objects.filter(parent=self).order_by("ordering"):
            progeny.extend(child.get_progeny(level + 1))
        return progeny

    def as_jstree(self):
        """formatted for jstree -> displayed as tree view in admin"""
        url = self.get_absolute_url()
        label = escape(self.label)
        if url is None:
            li_content = u'<a>{0}</a>'.format(label)
        else:
            li_content = u'<a href="{0}">{1}</a>'.format(url, label)

        children_li = [child.as_jstree() for child in self.get_children(allow_all=True)]

        return u'<li id="node_{0}" rel={3}>{1}<ul>{2}</ul></li>'.format(
            self.id,
            li_content, u''.join(children_li),
            "in_nav" if self.in_navigation and self.is_accessible() else "out_nav"
        )

    def _get_li_content(self, li_template, node_pos=0, total_nodes=0):
        """content when displayed in li html tag"""
        request = RequestManager().get_request()
        if li_template:
            template_ = li_template if hasattr(li_template, 'render') else get_template(li_template)
            context_dict = {
                'node': self,
                'node_pos': node_pos,
                'total_nodes': total_nodes,
                'STATIC_URL': settings.STATIC_URL,
            }
            if request:
                context = RequestContext(request, context_dict)
            else:
                context = Context(context_dict)
            return template_.render(context)
        else:
            url = self.get_absolute_url()
            if url is None:
                return u'<a>{0}</a>'.format(self.label)
            else:
                return u'<a href="{0}">{1}</a>'.format(url, self.label)

    def _get_ul_format(self, ul_template):
        """format ul tag"""
        if ul_template:
            template_ = ul_template if hasattr(ul_template, 'render') else get_template(ul_template)
            return template_.render({'node': self})
        else:
            return u'<ul>{0}</ul>'

    def _get_li_args(self, li_args):
        """li tag arguments"""
        if li_args:
            template_ = li_args if hasattr(li_args, 'render') else get_template(li_args)
            return template_.render({'node': self})
        else:
            return u''

    def as_navigation(self, **kwargs):
        """
        Display the node and his children as nested ul and li html tags.
        li_template is a custom template that can be passed
        """

        if not self.in_navigation or not self.is_accessible():
            return ""
        
        li_node = kwargs.get("li_node", None)
        li_template = kwargs.get("li_template", None)
        css_class = kwargs.get("css_class", "")
        ul_template = kwargs.get("ul_template", None)
        li_args = kwargs.get("li_args", None)
        active_class = kwargs.get("active_class", "active-node")
        node_pos = kwargs.get("node_pos", 0)
        total_nodes = kwargs.get("total_nodes", 0)

        children_li = [
            child.as_navigation(
                li_node=li_node,
                li_template=li_template,
                css_class=css_class,
                node_pos=node_pos + 1,
                total_nodes=self.get_children_count()
            )
            for child in self.get_children(in_navigation=True) if child.is_accessible()
        ]
        ul_format = self._get_ul_format(ul_template)
        children_html = ul_format.format(u''.join(children_li)) if children_li else ""

        args = self._get_li_args(li_args)
        if args.find("class=") < 0:
            css_class = u'class="{0} {1}"'.format(css_class, active_class if self.is_active_node() else "")
        else:
            css_class = ""

        if not li_node:
            return u'<li {0} {1}>{2}{3}</li>'.format(
                css_class, args, self._get_li_content(li_template), children_html
            )
        else:
            return self._get_li_content(li_node, node_pos, total_nodes)

    def as_breadcrumb(self, li_template=None, css_class=""):
        """iterate node by parents through root node"""
        html = self.parent.as_breadcrumb(li_template) if self.parent else u""
        return html + u'<li class="{0}">{1}</li>'.format(css_class, self._get_li_content(li_template))

    def children_as_navigation(self, li_template=None, css_class=""):
        """get children as navigation"""
        children_li = [
            u'<li class="{0}">{1}</li>'.format(css_class, child._get_li_content(li_template))
            for child in self.get_children(in_navigation=True) if child.is_accessible()
        ]
        return u''.join(children_li)

    def siblings_as_navigation(self, li_template=None, css_class=""):
        """get siblings as navigation"""
        siblings_li = [
            u'<li class="{0}">{1}</li>'.format(css_class, sibling._get_li_content(li_template))
            for sibling in self.get_siblings(in_navigation=True) if sibling.is_accessible()
        ]
        return u''.join(siblings_li)

    def check_new_navigation_parent(self, parent_id):
        """check if parent is valid"""
        if parent_id == self.id:
            raise ValidationError(_(u'A node can not be its own parent'))

        if parent_id:
            cur_node = NavNode.objects.get(id=parent_id)
            while cur_node:
                if cur_node.id == self.id:
                    raise ValidationError(_(u'A node can not be child of its own child'))
                cur_node = cur_node.parent


class ArticleCategory(models.Model):
    """Article category"""
    name = models.CharField(_(u'name'), max_length=100)
    slug = AutoSlugField(populate_from='name', max_length=100, unique=True)
    ordering = models.IntegerField(_(u'ordering'), default=0)
    in_rss = models.BooleanField(
        _(u'in rss'), default=False,
        help_text=_(u"The articles of this category will be listed in the main rss feed")
    )
    sites = models.ManyToManyField(Site, verbose_name=_(u'site'), default=[settings.SITE_ID])
    pagination_size = models.IntegerField(
        default=0,
        verbose_name=_(u'pagination size'),
        help_text=_(u"The number of articles to display in a category page. If 0, use default")
    )

    def __unicode__(self):
        return self.name
    
    def can_view_category(self, user):
        """perms"""
        return True

    def get_absolute_url(self):
        """url"""
        return reverse('coop_cms_articles_category', args=[self.slug])
    
    def get_articles_qs(self):
        """articles of category as queryset"""
        return get_article_class().objects.filter(
            sites__id=settings.SITE_ID, category=self, publication=BaseArticle.PUBLISHED
        ).distinct().order_by('publication_date')

    class Meta:
        verbose_name = _(u'article category')
        verbose_name_plural = _(u'article categories')
        
    def save(self, *args, **kwargs):
        """save"""
        is_new = not bool(self.id)
        ret = super(ArticleCategory, self).save(*args, **kwargs)
        
        if is_new:
            site = Site.objects.get(id=settings.SITE_ID)
            self.sites.add(site)
            super(ArticleCategory, self).save()

        return ret


class BaseNavigable(TimeStampedModel):
    """Base class for anything which can be in Navigation"""

    class Meta:
        abstract = True

    def is_accessible(self):
        """returns True if the content can be accessed. It most cases, it should be overridden"""
        return True

    def _get_navigation_parent(self):
        """getter for parent"""
        content_type = ContentType.objects.get_for_model(self.__class__)
        nodes = NavNode.objects.filter(object_id=self.id, content_type=content_type)
        if nodes.count():
            node = nodes[0]
            if node.parent:
                return node.parent.id
            else:
                return -node.tree.id
        else:
            return None

    def _set_navigation_parent(self, value):
        """setter for parent"""
        content_type = ContentType.objects.get_for_model(self.__class__)
        if value is not None:
            if value < 0:
                tree_id = -value
                tree = get_navtree_class().objects.get(id=tree_id)
                parent = None
            else:
                parent = NavNode.objects.get(id=value)
                tree = parent.tree

            create_navigation_node(content_type, self, tree, parent)

    navigation_parent = property(
        _get_navigation_parent, _set_navigation_parent, doc=_(u"set the parent in navigation.")
    )

    def save(self, do_not_create_nav=False, *args, **kwargs):
        """save"""
        ret = super(BaseNavigable, self).save(*args, **kwargs)
        if not do_not_create_nav:
            parent_id = getattr(self, '_navigation_parent', None)
            if parent_id is not None:
                self.navigation_parent = parent_id
        return ret


def get_logo_folder(article, filename):
    """where to put logo image file"""
    try:
        img_root = settings.CMS_ARTICLE_LOGO_FOLDER
    except AttributeError:
        img_root = 'cms_logos'
    basename = os.path.basename(filename)
    return u'{0}/{1}/{2}'.format(img_root, article.id, basename)


class BaseArticle(BaseNavigable):
    """An article : static page, blog item, ..."""

    DRAFT = 0
    PUBLISHED = 1
    ARCHIVED = 2

    PUBLICATION_STATUS = (
        (DRAFT, _(u'Draft')),
        (PUBLISHED, _(u'Published')),
        (ARCHIVED, _(u'Archived')),
    )

    slug = models.CharField(
        max_length=100, unique=True, db_index=True, blank=False, null=True, validators=[validate_slug]
    )
    title = models.TextField(_(u'title'), default='', blank=True)
    subtitle = models.TextField(_(u'subtitle'), default='', blank=True)
    content = models.TextField(_(u'content'), default='', blank=True)
    publication = models.IntegerField(_(u'publication'), choices=PUBLICATION_STATUS, default=PUBLISHED)
    template = models.CharField(_(u'template'), max_length=200, default='', blank=True)
    logo = models.ImageField(upload_to=get_logo_folder, blank=True, null=True, default='')
    temp_logo = models.ImageField(upload_to=get_logo_folder, blank=True, null=True, default='')
    summary = models.TextField(_(u'Summary'), blank=True, default='')
    category = models.ForeignKey(
        ArticleCategory, verbose_name=_(u'Category'), blank=True, null=True, default=None,
        related_name="%(app_label)s_%(class)s_rel"
    )
    in_newsletter = models.BooleanField(
        _(u'In newsletter'), default=True,
        help_text=_(u'Make this article available for newsletters.')
    )
    homepage_for_site = models.ForeignKey(
        Site, verbose_name=_(u'Homepage for site'), blank=True, null=True, default=None,
        related_name="homepage_article"
    )
    headline = models.BooleanField(
        _(u"Headline"), default=False,
        help_text=_(u'Make this article appear on the home page')
    )
    publication_date = models.DateTimeField(_(u"Publication date"), default=datetime.now)
    sites = models.ManyToManyField(Site, verbose_name=_(u'site'), default=[settings.SITE_ID])
    login_required = models.BooleanField(
        default=False,
        verbose_name=_(u'login required'),
        help_text=_(u'If true, only user with login/password will able to access the article')
    )
    
    @property
    def is_homepage(self):
        """True if is the homepage of the current site"""
        site_settings = SiteSettings.objects.get_or_create(site=Site.objects.get_current())[0]
        try:
            if homepage_no_redirection():
                return site_settings.homepage_article == self.slug
            else:
                return site_settings.homepage_url == self.get_absolute_url()
        except NoReverseMatch:
            return False

    def is_draft(self):
        """True if draft"""
        return self.publication == BaseArticle.DRAFT
    
    def is_archived(self):
        """True if archived"""
        return self.publication == BaseArticle.ARCHIVED
    
    def is_published(self):
        """True if published"""
        return self.publication == BaseArticle.PUBLISHED
    
    def next_in_category(self):
        """iterate by category"""
        if self.category:
            try:
                return get_article_class().objects.filter(
                    sites__id=settings.SITE_ID,
                    category=self.category,
                    publication=BaseArticle.PUBLISHED,
                    publication_date__gt=self.publication_date
                ).order_by('publication_date')[0]
            except IndexError:
                pass
        
    def previous_in_category(self):
        """iterate by category"""
        if self.category:
            try:
                return get_article_class().objects.filter(
                    sites__id=settings.SITE_ID, category=self.category,
                    publication=BaseArticle.PUBLISHED,
                    publication_date__lt=self.publication_date
                ).order_by('-publication_date')[0]
            except IndexError:
                pass

    def logo_thumbnail(self, temp=False, logo_size=None, logo_crop=None):
        """logo as thumbnail"""
        logo = self.temp_logo if (temp and self.temp_logo) else self.logo
        size = logo_size or get_article_logo_size(self)
        logo_file = None
        if logo:
            try:
                logo_file = logo.file
            except IOError:
                pass
        if not logo_file:
            logo_file = self._get_default_logo()
        crop = logo_crop or get_article_logo_crop(self)
        try:
            return sorl_thumbnail.backend.get_thumbnail(logo_file, size, crop=crop)
        except IOError:
            return logo_file
        
    def get_headline_image(self):
        """headline image"""
        img_size = get_headline_image_size(self)
        crop = get_headline_image_crop(self)
        return self.logo_thumbnail(logo_size=img_size, logo_crop=crop).url

    def _get_default_logo(self):
        """default logo"""
        # copy from static to media in order to use sorl thumbnail without raising a suspicious operation
        filename = get_default_logo()
        media_filename = os.path.normpath(settings.MEDIA_ROOT + '/coop_cms/' + filename)
        if not os.path.exists(media_filename):
            file_dir = os.path.dirname(media_filename)
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
            static_filename = finders.find(filename)
            shutil.copyfile(static_filename, media_filename)
        return File(open(media_filename, 'r'))

    def logo_list_display(self):
        """logo in article admin"""
        if self.logo:
            thumb = sorl_thumbnail.backend.get_thumbnail(self.logo.file, ADMIN_THUMBS_SIZE)
            return '<img width="%s" src="%s" />' % (thumb.width, thumb.url)
        else:
            return _(u"No Image")
    logo_list_display.short_description = _(u"logo")
    logo_list_display.allow_tags = True

    class Meta:
        verbose_name = _(u"article")
        verbose_name_plural = _(u"articles")
        abstract = True

    def __unicode__(self):
        return u"{0} {1}".format(dehtml(self.title), dehtml(self.subtitle)).strip()

    def save(self, *args, **kwargs):
        """save"""
        if hasattr(self, "_cache_slug"):
            delattr(self, "_cache_slug")
        
        # autoslug localized title for creating locale_slugs
        if (not self.title) and (not self.slug):
            raise InvalidArticleError(u"coop_cms.Article: slug can not be empty")
            
        if is_localized():
            from modeltranslation.utils import build_localized_fieldname  # pylint: disable=F0401
            for lang_code in [lang[0] for lang in settings.LANGUAGES]:

                loc_title_var = build_localized_fieldname('title', lang_code)
                locale_title = getattr(self, loc_title_var, '')
            
                loc_slug_var = build_localized_fieldname('slug', lang_code)
                locale_slug = getattr(self, loc_slug_var, '')

                if locale_title and not locale_slug:
                    slug = self.get_unique_slug('slug', locale_title, lang_code)
                    setattr(self, loc_slug_var, slug)
        else:
            if not self.slug:
                self.slug = self.get_unique_slug('slug', self.title)
        
        is_new = not bool(self.id)
        ret = super(BaseArticle, self).save(*args, **kwargs)
        
        if is_new:
            site = Site.objects.get(id=settings.SITE_ID)
            self.sites.add(site)
            ret = super(BaseArticle, self).save(do_not_create_nav=True)

        return ret

    def _does_slug_exist(self, slug_field, slug):
        """generate slug"""
        article_class = get_article_class()

        if is_localized():
            from modeltranslation.utils import build_localized_fieldname  # pylint: disable=F0401
            slug_fields = []
            for lang_code in [lang[0] for lang in settings.LANGUAGES]:
                loc_slug_var = build_localized_fieldname(slug_field, lang_code)
                slug_fields.append(loc_slug_var)
        else:
            slug_fields = (slug_field,)

        for slug_field in slug_fields:
            try:
                lookup = {slug_field: slug}
                if self.id:
                    article_class.objects.get(Q(**lookup) & ~Q(id=self.id))
                else:
                    article_class.objects.get(**lookup)
                # the slug exists in one language: we can not use it, try another one
                return True

            except article_class.DoesNotExist:
                # Ok this slug is not used: try next language
                pass

        return False

    def get_unique_slug(self, slug_field, title, lang=None):
        """unique slug"""
        # no html in title
        title = dehtml(title)
        slug = slugify(title, lang)
        next_suffix, origin_slug = 2, slug
        slug_exists = True

        while slug_exists:
            # Check that this slug doesn't already exist
            # The slug must be unique for all sites

            slug_exists = self._does_slug_exist(slug_field, slug)
            
            if slug_exists:
                # oups the slug is already used: change it and try again
                next_suffix_len = len(str(next_suffix))
                safe_slug = origin_slug[:(100 - next_suffix_len)]
                slug = u"{0}{1}".format(safe_slug, next_suffix)
                next_suffix += 1

        return slug
        
    def template_name(self):
        """template name"""
        possible_templates = get_article_templates(self, None)
        for (template, name) in possible_templates:
            if template == self.template:
                return name
        return u"?"

    def get_label(self):
        """label for navigation"""
        return self.title

    def _get_slug(self):
        """get slug"""
        from modeltranslation.utils import build_localized_fieldname
        slug = self.slug
        if not slug:
            for lang_code in [lang[0] for lang in settings.LANGUAGES]:
                key = build_localized_fieldname('slug', lang_code)
                slug = getattr(self, key)
                if slug:
                    break
        return slug

    def get_absolute_url(self):
        """url for viewing"""
        if homepage_no_redirection() and self.is_homepage:
            return reverse('coop_cms_homepage')
        return reverse('coop_cms_view_article', args=[self._get_slug()])

    def get_edit_url(self):
        """url for editing"""
        return reverse('coop_cms_edit_article', args=[self._get_slug()])

    def get_cancel_url(self):
        """url to go on cancel"""
        return reverse('coop_cms_cancel_edit_article', args=[self._get_slug()])

    def get_publish_url(self):
        """url for publication"""
        return reverse('coop_cms_publish_article', args=[self._get_slug()])

    def _can_change(self, user):
        """has change perm"""
        content_type = ContentType.objects.get_for_model(get_article_class())
        perm = '{0}.change_{1}'.format(content_type.app_label, content_type.model)
        return user.has_perm(perm)

    def can_view_article(self, user):
        """view perm"""
        if not self.is_published():
            return self.can_edit_article(user)
        else:
            return True
        
    def can_edit_article(self, user):
        """edit perm"""
        return self._can_change(user)

    def can_publish_article(self, user):
        """publish perm"""
        return self._can_change(user)

    def is_accessible(self):
        """returns True if the content can be accessed. It most cases, it should be overridden"""

        current_site = Site.objects.get_current()

        if current_site not in self.sites.all():
            return False

        if self.is_draft():
            if is_requestprovider_installed():
                try:
                    http_request = RequestManager().get_request()
                    return http_request.user.is_staff
                except RequestNotFound:
                    pass
            return False

        if self.is_archived():
            return False

        return True


class Link(BaseNavigable):
    """Link to a given url"""
    title = models.CharField(_(u'Title'), max_length=200, default=_(u"title"))
    url = models.CharField(_(u'URL'), max_length=200)
    sites = models.ManyToManyField(Site, blank=True)

    def get_absolute_url(self):
        """url"""
        if is_localized():
            # parsed_url = scheme, netloc, path, params, query, fragment
            parsed_url = urlparse.urlparse(self.url)
            scheme = parsed_url[0]
            if not scheme:
                # the urls doesn't starts with http://, so it's a url managed by the site
                locale = get_language()
                return make_locale_path(self.url, locale)
        return self.url

    def get_label(self):
        """label for navigation"""
        # parsed_url = scheme, netloc, path, params, query, fragment
        parsed_url = urlparse.urlparse(self.url)
        scheme, netloc, path = parsed_url[0], parsed_url[1], parsed_url[2]
        if scheme:
            return u"{0}{1}".format(netloc, path)
        return self.url

    def is_accessible(self):
        """returns True if the content can be accessed. It most cases, it should be overridden"""
        current_site = Site.objects.get_current()
        if current_site not in self.sites.all():
            return False
        return True

    def __unicode__(self):
        return dehtml(self.title)

    class Meta:
        verbose_name = _(u"link")
        verbose_name_plural = _(u"links")


class MediaFilter(models.Model):
    """make possible to group images: filter in media library, photo album"""
    name = models.CharField(_('name'), max_length=100)
    
    class Meta:
        verbose_name = _(u'media filter')
        verbose_name_plural = _(u'media filters')
        
    def __unicode__(self):
        return self.name


class ImageSize(models.Model):
    """Image size for auto resizing"""
    name = models.CharField(_(u'name'), max_length=100)
    size = models.CharField(_(u'size'), max_length=100)
    crop = models.CharField(_(u'crop'), max_length=100, blank=True, default="")
    
    class Meta:
        verbose_name = _(u'Image size')
        verbose_name_plural = _(u'Image sizes')
        
    def __unicode__(self):
        return u"{0} ({1}{2})".format(self.name, self.size, (" "+self.crop if self.crop else ""))


class Media(TimeStampedModel):
    """Base class for something you can put in Media library"""
    name = models.CharField(_('name'), max_length=200, blank=True, default='')
    filters = models.ManyToManyField(MediaFilter, blank=True, default=None, verbose_name=_(u"filters"))
    ordering = models.IntegerField(_(u"ordering"), default=100)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class Image(Media):
    """An image in media library"""
    file = models.ImageField(_(u'file'), upload_to=get_img_folder)
    size = models.ForeignKey(ImageSize, default=None, blank=True, null=True, verbose_name=_(u"size"))
    copyright = models.CharField(max_length=200, verbose_name=_(u'copyright'), blank=True, default='')

    def __unicode__(self):
        return self.name

    def clear_thumbnails(self):
        """clear thumbnails"""
        sorl_delete(self.file.file, delete_file=False)    
    
    def as_thumbnail(self):
        """convert to thumbnail"""
        try:
            return sorl_thumbnail.backend.get_thumbnail(self.file.file, "64x64", crop='center')
        except IOError:
            return self.file
        
    def admin_image(self):
        """admin"""
        return '<img src="{0}"/>'.format(self.as_thumbnail().url)
    admin_image.allow_tags = True
    admin_image.short_description = _(u"Image")

    def get_absolute_url(self):
        """url"""
        if not self.size:
            max_width = get_max_image_width(self)
            max_width = int(max_width) if max_width else 0
            if max_width and (max_width < self.file.width):
                try:
                    url = sorl_thumbnail.backend.get_thumbnail(self.file.file, str(max_width), upscale=False).url
                    return url
                except (IOError, ThumbnailParseError):
                    return self.file.url
            else:
                return self.file.url
        try:
            crop = self.size.crop or None
            url = sorl_thumbnail.backend.get_thumbnail(self.file.file, self.size.size, crop=crop).url
            return url
        except (IOError, ThumbnailParseError):
            return self.file.url

    class Meta:
        verbose_name = _(u'image')
        verbose_name_plural = _(u'images')


def get_doc_folder(document, filename):
    """where to store this file. If private in a different folder which must be protected by web server"""
    if not document.is_private:
        doc_root = getattr(settings, 'DOCUMENT_FOLDER', 'documents/public')
    else:
        doc_root = getattr(settings, 'PRIVATE_DOCUMENT_FOLDER', 'documents/private')

    filename = os.path.basename(filename)
    # This is required for x-sendfile
    name, ext = os.path.splitext(filename)
    filename = slugify(name) + ext

    return u'{0}/{1}'.format(doc_root, filename)


class Document(Media):
    """file in media library"""

    def __unicode__(self):
        return self.name

    file = models.FileField(_('file'), upload_to=get_doc_folder)
    is_private = models.BooleanField(
        _('is private'), default=False,
        help_text=_(u"Check this if you do not want to publish this document to all users")
    )
    category = models.ForeignKey(ArticleCategory, blank=True, null=True, default=None, verbose_name=_(u'category'))

    def can_download_file(self, user):
        """is user allowed to download"""
        return user.is_authenticated()

    def get_download_url(self):
        """download url"""
        if self.is_private:
            return reverse('coop_cms_download_doc', args=[self.id])
        else:
            return self.file.url

    def get_ico_url(self, icotype):
        """icon associated to the document"""
        ext = os.path.splitext(self.file.name)[1]
        ext = ext[1:].lower()  # remove leading dot
        supported_ext = (
            'pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'png', 'jpg', 'gif', 'ppt', 'pps', 'mp3', 'ogg', 'html',
            'rtf', 'zip', 'avi', 'mov', 'mp4',
        )
        if ext in supported_ext:
            return settings.STATIC_URL + u'img/filetypes/' + icotype + '/{0}.png'.format(ext)
        else:
            return settings.STATIC_URL + u'img/filetypes/' + icotype + '/default.png'

    def get_block_url(self):
        """icon url"""
        return self.get_ico_url('bloc')

    def get_fileicon_url(self):
        """icon url"""
        return self.get_ico_url('icon')

    class Meta:
        verbose_name = _(u'document')
        verbose_name_plural = _(u'documents')


class PieceOfHtml(models.Model):
    """This is a block of text thant can be added to a page and edited on it"""
    div_id = models.CharField(verbose_name=_(u"identifier"), max_length=100, db_index=True)
    content = models.TextField(_(u"content"), default="", blank=True)
    extra_id = models.CharField(
        verbose_name=_(u"extra identifier"), blank=True, default="", max_length=100, db_index=True
    )

    def __unicode__(self):
        return u" ".join([self.div_id, self.extra_id])

    class Meta:
        verbose_name = _(u'piece of HTML')
        verbose_name_plural = _(u'pieces of HTML')


def remove_from_navigation(sender, instance, **kwargs):
    """delete node when content object is deleted"""
    if hasattr(instance, 'id'):
        try:
            content_type = ContentType.objects.get_for_model(instance)
            nodes = NavNode.objects.filter(content_type=content_type, object_id=instance.id)
            nodes.delete()
        except ContentType.DoesNotExist:
            pass

pre_delete.connect(remove_from_navigation)


class NewsletterItem(models.Model):
    """Something which is in a newsletter"""
    content_type = models.ForeignKey(ContentType, verbose_name=_("content_type"))
    object_id = models.PositiveIntegerField(verbose_name=_("object id"))
    content_object = GenericForeignKey('content_type', 'object_id')
    ordering = models.IntegerField(verbose_name=_("ordering"), default=0)

    class Meta:
        unique_together = (("content_type", "object_id"),)
        verbose_name = _(u'newsletter item')
        verbose_name_plural = _(u'newsletter items')
        ordering = ['ordering']

    def __unicode__(self):
        try:
            return u'{0}: {1}'.format(self.content_type, self.content_object)
        except AttributeError:
            return u''


def on_delete_newsletterable_item(sender, instance, **kwargs):
    """delete item when content object is deleted"""
    if hasattr(instance, 'id'):
        try:
            content_type = ContentType.objects.get_for_model(instance)
            item = NewsletterItem.objects.get(content_type=content_type, object_id=instance.id)
            item.delete()
        except (NewsletterItem.DoesNotExist, ContentType.DoesNotExist):
            pass
pre_delete.connect(on_delete_newsletterable_item)


def create_newsletter_item(instance):
    """Create a newsletter item automatically"""
    content_type = ContentType.objects.get_for_model(instance)
    if getattr(instance, 'in_newsletter', True):
        # Create a newsletter item automatically
        # An optional 'in_newsletter' field can skip the automatic creation if set to False
        return NewsletterItem.objects.get_or_create(content_type=content_type, object_id=instance.id)
    elif hasattr(instance, 'in_newsletter'):
        # If 'in_newsletter' field exists and is False
        # We delete the Item if exists
        try:
            item = NewsletterItem.objects.get(content_type=content_type, object_id=instance.id)
            item.delete()
            return None, True
        except NewsletterItem.DoesNotExist:
            return None, False


def on_create_newsletterable_instance(sender, instance, created, raw, **kwargs):
    """create automatically a newsletter item for every objects configured as newsletter_item"""
    if sender in get_newsletter_item_classes():
        create_newsletter_item(instance)

post_save.connect(on_create_newsletterable_instance)


class Newsletter(TimeStampedModel):
    """Newsletter"""
    subject = models.CharField(max_length=200, verbose_name=_(u'subject'), blank=True, default="")
    content = models.TextField(_(u"content"), default="<br>", blank=True)
    items = models.ManyToManyField(NewsletterItem, blank=True)
    template = models.CharField(_(u'template'), max_length=200, default='', blank=True)
    site = models.ForeignKey(Site, verbose_name=_(u'site'), default=settings.SITE_ID)
    source_url = models.URLField(verbose_name=_(u'source url'), default="", blank=True)
    is_public = models.BooleanField(default=False, verbose_name=_(u'is_public'))
    newsletter_date = models.DateField(blank=True, null=True, default=None, verbose_name=_(u'newsletter date'))

    def get_items(self):
        """associated items"""
        return [item.content_object for item in self.items.all()]

    def get_items_by_category(self):
        """items by category"""
        items = self.get_items()

        def sort_by_category(item):
            """sort function"""
            category = getattr(item, 'category', None)
            if category:
                return category.ordering
            return 0

        items.sort(key=sort_by_category)
        return items

    def can_edit_newsletter(self, user):
        """perms"""
        return user.has_perm('coop_cms.change_newsletter')
        
    def get_site_prefix(self):
        """site prefix"""
        return "http://{0}".format(self.site.domain)

    def get_absolute_url(self):
        """url for viewing"""
        # force inline style
        return reverse('coop_cms_view_newsletter', args=[self.id]) + "?by_email=1"

    def get_edit_url(self):
        """url for editing"""
        return reverse('coop_cms_edit_newsletter', args=[self.id])

    def get_template_name(self):
        """template"""
        template = self.template
        if not template:
            template = 'coop_cms/newsletter.html'
        return template

    def __unicode__(self):
        return dehtml(self.subject).replace('\n', '')

    class Meta:
        verbose_name = _(u'newsletter')
        verbose_name_plural = _(u'newsletters')


class NewsletterSending(models.Model):
    """Schedule newsletter sending"""

    newsletter = models.ForeignKey(Newsletter)
    scheduling_dt = models.DateTimeField(_(u"scheduling date"), blank=True, default=None, null=True)
    sending_dt = models.DateTimeField(_(u"sending date"), blank=True, default=None, null=True)

    def __unicode__(self):
        return self.newsletter.subject

    class Meta:
        verbose_name = _(u'newsletter sending')
        verbose_name_plural = _(u'newsletter sendings')


class Alias(models.Model):
    """Alias : makes possinle to redirect an url ton another one"""

    CODE_CHOICES = (
        (301, _(u'301 - Permanent')),
        (302, _(u'302 - Non permanent')),
    )

    path = models.CharField(max_length=200)
    redirect_url = models.CharField(max_length=200, default="", blank=True)
    redirect_code = models.IntegerField(default=301, choices=CODE_CHOICES)
    sites = models.ManyToManyField(Site, blank=True, verbose_name=_(u'sites'))
    
    class Meta:
        verbose_name = _(u'Alias')
        verbose_name_plural = _(u'Aliases')
    
    def get_absolute_url(self):
        """urls"""
        return reverse('coop_cms_view_alias', args=[self.path])
    
    def __unicode__(self):
        return self.path

    def save(self, **kwargs):
        if self.path and self.path[-1] == u'/':
            self.path = self.path[:-1]
        return super(Alias, self).save(**kwargs)


class FragmentType(models.Model):
    """Type of fragments"""
    name = models.CharField(max_length=100, db_index=True, verbose_name=_(u"name"))
    allowed_css_classes = models.CharField(
        max_length=200, verbose_name=_(u"allowed css classes"), default="",
        help_text=_(u"the css classed proposed when editing a fragment. It must be separated by comas")
    )
    
    class Meta:
        verbose_name = _(u'Fragment type')
        verbose_name_plural = _(u'Fragment types')
        
    def __unicode__(self):
        return self.name


class FragmentFilter(models.Model):
    """filter fragments"""
    extra_id = models.CharField(max_length=100, db_index=True, verbose_name=_(u"extra_id"))
    
    class Meta:
        verbose_name = _(u'Fragment filter')
        verbose_name_plural = _(u'Fragment filters')
        
    def __unicode__(self):
        return self.extra_id


class Fragment(models.Model):
    """small piece of html which can be dynamically added to the page"""
    type = models.ForeignKey(FragmentType, verbose_name=_(u'fragment type'))
    name = models.CharField(max_length=100, db_index=True, verbose_name=_(u'name'))
    css_class = models.CharField(max_length=100, default=u"", blank=True, verbose_name=_(u'CSS class'))
    position = models.IntegerField(verbose_name=_("position"), default=0)
    content = models.TextField(default=u"", blank=True, verbose_name=_(u'content'))
    filter = models.ForeignKey(FragmentFilter, verbose_name=_(u'fragment filter'), blank=True, null=True, default=None)
    
    class Meta:
        verbose_name = _(u'Fragment')
        verbose_name_plural = _(u'Fragment')
        ordering = ("position", "id")
        
    def _can_change(self, user):
        """perms"""
        content_type = ContentType.objects.get_for_model(get_article_class())
        perm = '{0}.change_{1}'.format(content_type.app_label, content_type.model)
        return user.has_perm(perm)

    def can_add_fragment(self, user):
        """perms"""
        content_type = ContentType.objects.get_for_model(Fragment)
        perm = '{0}.add_{1}'.format(content_type.app_label, content_type.model)
        return user.has_perm(perm)

    def can_edit_fragment(self, user):
        """perms"""
        content_type = ContentType.objects.get_for_model(Fragment)
        perm = '{0}.change_{1}'.format(content_type.app_label, content_type.model)
        return user.has_perm(perm)
        
    def save(self, *args, **kwargs):
        """save"""
        if not self.id and not self.position:
            max_position = Fragment.objects.filter(
                type=self.type, filter=self.filter
            ).aggregate(Max('position'))['position__max'] or 0
            self.position = max_position + 1
        return super(Fragment, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"{0} {1} {2}".format(self.type, self.position, self.name)


class SiteSettings(models.Model):
    """site settings"""

    SITEMAP_ONLY_SITE = 1
    SITEMAP_ALL = 2

    SITEMAP_MODES = (
        (SITEMAP_ONLY_SITE, _(u"Only site articles")),
        (SITEMAP_ALL, _(u"All articles")),
    )

    site = models.OneToOneField(Site, verbose_name=_(u'site settings'))
    homepage_url = models.CharField(
        max_length=256, blank=True, default=u"", verbose_name=_(u'homepage URL'),
        help_text=_(u"if set, the homepage will be redirected to the given URL"), db_index=True
    )
    sitemap_mode = models.IntegerField(default=SITEMAP_ONLY_SITE, choices=SITEMAP_MODES)
    homepage_article = models.CharField(
        max_length=256, blank=True, default=u"", verbose_name=_(u'homepage article'),
        help_text=_(u"if set, the homepage will get the article with the given slug"), db_index=True
    )
    
    def __unicode__(self):
        return u"{0}".format(self.site)
    
    class Meta:
        verbose_name = _(u'Sites settings')
        verbose_name_plural = _(u'Site settings')
        ordering = ("site__id",)


def get_homepage_url():
    """returns the URL of the home page"""
    if not cms_no_homepage():
        site = Site.objects.get_current()
        # Try site settings
        try:
            site_settings = SiteSettings.objects.get(site=site)
            if site_settings.homepage_url:
                return site_settings.homepage_url
        except SiteSettings.DoesNotExist:
            pass


def get_homepage_article():
    """returns the URL of the home page"""
    if not cms_no_homepage():
        site = Site.objects.get_current()
        # Try site settings
        try:
            site_settings = SiteSettings.objects.get(site=site)
            if site_settings.homepage_article:
                return site_settings.homepage_article
        except SiteSettings.DoesNotExist:
            pass
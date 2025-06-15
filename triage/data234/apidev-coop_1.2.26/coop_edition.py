# -*- coding: utf-8 -*-
"""
coop_edition template tags
used for magic form
"""

from django import VERSION as DJANGO_VERSION
from django import template
from django.forms.formsets import BaseFormSet
from django.template import Context
from django.template.base import TextNode, VariableNode
from django.template.context_processors import csrf
from django.template.loader import get_template, TemplateDoesNotExist
from django.template.loader_tags import IncludeNode
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from coop_html_editor.templatetags.html_editor_utils import InlineHtmlEditNode, InlineHtmlMultipleEditNode

from coop_cms.models import PieceOfHtml, BaseArticle, Fragment, FragmentType, FragmentFilter
from coop_cms.settings import get_article_class
from coop_cms.utils import get_text_from_template, slugify

register = template.Library()


class DummyEngine(object):
    """Used for monkey patching Context"""
    debug = False
    string_if_invalid = ''


class DummyEditableForm(object):
    """Used for monkey patching Context"""
    is_inline_editable = True


class PieceOfHtmlEditNode(InlineHtmlEditNode):
    """Template node for editing a PieceOfHtml"""

    def render(self, context):
        """convert to html"""
        form = context.get('form', None) or context.get('formset', None)
        if form:
            context.dicts[0]['inline_html_edit'] = _is_inline_editable(form)
        return super(PieceOfHtmlEditNode, self).render(context)


@register.tag
def coop_piece_of_html(parser, token):
    """template tag"""
    args = token.split_contents()
    div_id = args[1]
    read_only = False
    extra_id = ""
    if len(args) > 2:
        for item in args[2:]:
            if 0 == item.find("extra_id="):
                extra_id = item.replace("extra_id=", '')
        
        read_only = (args[2] == "read-only")
    
    lookup_args = {'div_id': div_id}
    if extra_id:
        lookup_args.update({'extra_id': extra_id})
    
    return PieceOfHtmlEditNode(PieceOfHtml, lookup_args, 'content', read_only)


class FragmentEditNode(InlineHtmlMultipleEditNode):
    """Template Node for Fragment edition"""

    def __init__(self, lookup, kwargs=None):
        super(FragmentEditNode, self).__init__(Fragment, lookup, 'content')
        self._edit_mode = False
        self.fragment_filter = None
        self.kwargs = kwargs or {}
        self.fragment_type = None

    def _get_objects(self, lookup):
        """get the fragment"""
        self.fragment_type = FragmentType.objects.get_or_create(name=lookup['name'])[0]
        queryset = Fragment.objects.filter(type=self.fragment_type)
        if 'extra_id' in lookup:
            self.fragment_filter = FragmentFilter.objects.get_or_create(extra_id=lookup['extra_id'])[0]
            queryset = queryset.filter(filter=self.fragment_filter)
        return queryset
    
    def _get_object_lookup(self, obj):
        """get object lookup"""
        return {"id": obj.id}

    def _pre_object_render(self, obj):
        """call before rendering an object"""
        return u'<div class="coop-fragment {0}" rel="{1}">'.format(obj.css_class, obj.id)
    
    def _post_object_render(self, obj):
        """call after rendering an object"""
        return u'</div>'
    
    def _object_render(self, idx, obj, context):
        """convert object to html"""
        value = getattr(obj, self._field_name)
        template_name = self.kwargs.get('template_name', '')
        if template_name:
            template_name = self._resolve_arg(template_name, context)
            template_ = get_template(template_name)
            objects_count = self.get_objects_to_render_count()
            object_content = template_.render(template.Context({
                'css_class': obj.css_class,
                'name': obj.name,
                'slug': slugify(obj.name),
                'id': obj.id,
                'index': idx,
                'objects_count': objects_count,
                'fragment': self._render_value(context, self._get_object_lookup(obj), value),
                'form': DummyEditableForm() if self._edit_mode else None,
            }))
        else:
            object_content = self._pre_object_render(obj)
            object_content += self._render_value(context, self._get_object_lookup(obj), value)
            object_content += self._post_object_render(obj)
        return object_content
    
    def render(self, context):
        """convert to html"""
        self._edit_mode = False
        form = context.get('form', None) or context.get('formset', None)
        if getattr(form, 'is_inline_editable', False):
            context.dicts[0]['inline_html_edit'] = True
            self._edit_mode = True
        html = super(FragmentEditNode, self).render(context)
        filter_id = self.fragment_filter.id if self.fragment_filter else ""
        if self._edit_mode:
            html_layout = u'<div style="display: none; visibility: hidden;" class="coop-fragment-type" '
            html_layout += u'rel="{0}" data-filter="{2}">{1}</div>'
            pre_html = html_layout.format(
                self.fragment_type.id, self.fragment_type.name, filter_id
            )
        else:
            pre_html = u''
        return pre_html + html


@register.tag
def coop_fragments(parser, token):
    """templatetag"""
    args = token.split_contents()
    lookup = {'name': args[1]}
    extra_id_found = False
    if len(args) > 2:
        args2 = args[2]
        if args2.find("=") < 0:
            lookup["extra_id"] = args2
            extra_id_found = True

    kwargs = {}
    start_index = 2 if extra_id_found else 1
    for arg in args[start_index:]:
        if arg.find("=") > 0:
            key, value = arg.split('=')
            if key == "extra_id" and not extra_id_found:
                lookup["extra_id"] = value
                extra_id_found = True
            else:
                kwargs[key] = value
    return FragmentEditNode(lookup, kwargs)


class ArticleSummaryEditNode(InlineHtmlEditNode):
    """edit the article summary"""

    def render(self, context):
        """to html"""
        form = context.get('form', None)
        if form and getattr(form, 'is_inline_editable', False):
            context.dicts[0]['inline_html_edit'] = True
        return super(ArticleSummaryEditNode, self).render(context)


@register.tag
def article_summary_edit(parser, token):
    """template tag"""
    article_class = get_article_class()
    article_id = token.split_contents()[1]
    return ArticleSummaryEditNode(article_class, {'id': article_id}, 'summary')


class ArticleTitleNode(template.Node):
    """article title tag"""

    def render(self, context):
        """to html"""
        is_edition_mode = context.get('form', None) is not None
        article = context.get('article')
        return u"{0}{1}{2}{3}".format(
            article.title,
            _(u" [EDITION]") if is_edition_mode else u"",
            _(u" [DRAFT]") if article.publication == BaseArticle.PUBLISHED else u"",
            _(u" [ARCHIVED]") if article.publication == BaseArticle.ARCHIVED else u"",
        )


@register.tag
def article_title(parser, token):
    """article title tag"""
    return ArticleTitleNode()


class CmsFormMediaNode(template.Node):
    """generate html for getting required js and css"""

    def render(self, context):
        form = context.get('form', None)
        formset = context.get('formset', None)

        if form or formset:
            template_ = template.Template("{{form.media}}")
            html = template_.render(template.Context({'form': form or formset}))
            # django 1.5 fix : " are escaped as &quot; and cause script tag
            # for aloha to be broken
            return html.replace("&quot;", '"') 
        else:
            return ""


@register.tag
def cms_form_media(parser, token):
    """generate html for getting required js and css"""
    return CmsFormMediaNode()


def _extract_if_node_args(parser, token):
    """utility for if else endif type of tags"""
    nodelist_true = parser.parse(('else', 'endif'))
    token = parser.next_token()
    if token.contents == 'else':
        nodelist_false = parser.parse(('endif',))
        parser.delete_first_token()
    else:
        nodelist_false = template.NodeList()
    return nodelist_true, nodelist_false


def _is_inline_editable(form):
    """
    :param form: form or formset
    :return: True if edit mode, False if not
    """
    if isinstance(form, BaseFormSet):
        for form_item in form:
            if getattr(form_item, 'is_inline_editable', False):
                return True
    else:
        if getattr(form, 'is_inline_editable', False):
            return True
    return False


class IfCmsEditionNode(template.Node):
    """Do something if edition mode"""

    def __init__(self, nodelist_true, nodelist_false):
        self.nodelist_true = nodelist_true
        self.nodelist_false = nodelist_false

    def __iter__(self):
        for node in self.nodelist_true:
            yield node
        for node in self.nodelist_false:
            yield node

    def _check_condition(self, context):
        """check condition of the if"""
        form = context.get('form', None) or context.get('formset', None)
        if form:
            return _is_inline_editable(form)
        return False

    def render(self, context):
        """to html"""
        if self._check_condition(context):
            return self.nodelist_true.render(context)
        else:
            return self.nodelist_false.render(context)


@register.tag
def if_cms_edition(parser, token):
    """Do something if edition mode"""
    nodelist_true, nodelist_false = _extract_if_node_args(parser, token)
    return IfCmsEditionNode(nodelist_true, nodelist_false)


class IfNotCmsEditionNode(IfCmsEditionNode):
    """Do something if not edition mode"""
    def _check_condition(self, context):
        return not super(IfNotCmsEditionNode, self)._check_condition(context)


@register.tag
def if_not_cms_edition(parser, token):
    """Do something if not edition mode"""
    nodelist_true, nodelist_false = _extract_if_node_args(parser, token)
    return IfNotCmsEditionNode(nodelist_true, nodelist_false)


CMS_FORM_TEMPLATE = """
<form id="cms_form" enctype="multipart/form-data"  method="POST" action="{{post_url}}">{% csrf_token %}
    {% include "coop_cms/_form_error.html" with errs=form.non_field_errors %}
    {{inner}} <input type="submit" style="display: none"> </form>
"""


class SafeWrapper(object):
    """This manages display of object in edit or non-edit context"""

    def __init__(self, wrapped, logo_size=None, logo_crop=None):
        self._wrapped = wrapped
        self._logo_size = logo_size
        self._logo_crop = logo_crop

    def __getattr__(self, field):
        value = getattr(self._wrapped, field)
        if field == 'logo':
            src = getattr(self._wrapped, 'logo_thumbnail')(False, self._logo_size, self._logo_crop)
            if src:
                try:
                    template_ = get_template("coop_cms/widgets/_img_logo.html")
                    value = template_.render(
                        template.Context(
                            {
                                'url': src.url,
                                'extra_classes': get_text_from_template("coop_cms/widgets/_imageedit_cssclass.html")
                            }
                        )
                    )
                except TemplateDoesNotExist:
                    value = u'<img class="logo" src="{0}" />'.format(src.url)
            else:
                value = u''
            return mark_safe(value)
        elif callable(value):
            try:
                return value()
            except KeyError:
                pass
        elif type(value) in (unicode, str):
            return mark_safe(value)
        return value


class FormWrapper(object):
    """This manages display of object in edit or non-edit context"""

    def __init__(self, form, obj, logo_size=None, logo_crop=None):
        self._form = form
        self._obj = obj
        if logo_size:
            self._form.set_logo_size(logo_size, logo_crop)

    def __getitem__(self, field, logo_size=None):
        """get attribute"""
        if field in self._form.fields.keys():
            template_ = template.Template("""
                    {%% with form.%s.errors as errs %%}
                    {%% include "coop_cms/_form_error.html" %%}{%% endwith %%}{{form.%s}}
                """ % (field, field))
            return template_.render(template.Context({'form': self._form}))
        else:
            return getattr(self._obj, field)


class CmsEditNode(template.Node):
    """cms_edit -> manages edition of object"""

    def __init__(self, nodelist_content, var_name, logo_size=None, logo_crop=None):
        self.var_name = var_name
        self.nodelist_content = nodelist_content
        self._logo_size = logo_size.strip("'").strip('"') if logo_size else None
        self._logo_crop = logo_crop.strip("'").strip('"') if logo_crop else None
        self._render_logo_size = self._logo_size and (self._logo_size == logo_size)
        self._render_logo_crop = self._logo_crop and (self._logo_crop == logo_crop)
        self.post_url = ""

    def __iter__(self):
        for node in self.nodelist_content:
            yield node

    def _render_nodes(self, context, inner_context, safe_context):
        """Replace nested nodes with proper content"""
        managed_node_types = [
            TextNode,
            template.defaulttags.IfNode,
            IfCmsEditionNode,
            IfNotCmsEditionNode,
            template.defaulttags.ForNode,
        ]

        nodes_content = ""
        for node in self.nodelist_content:

            if any([isinstance(node, node_type) for node_type in managed_node_types]):
                local_context = Context(safe_context)
                if hasattr(context, 'template'):
                    local_context.template = context.template
                content = node.render(local_context)

            elif node.__class__.__name__ == 'MediaListNode':
                content = node.render(context)
                safe_context[node.var_name] = context.get(node.var_name)
                inner_context[node.var_name] = context.get(node.var_name)

            elif node.__class__.__name__ == 'AssignmentNode':
                content = node.render(context)
                safe_context[node.target_var] = context.get(node.target_var)
                inner_context[node.target_var] = context.get(node.target_var)

            elif DJANGO_VERSION >= (1, 8, 0) and isinstance(node, IncludeNode):
                # monkey patching for django 1.8
                template_name = node.template.resolve(context)
                node.template = get_template(template_name)
                node.template.resolve = lambda s, c: s
                context_dict = inner_context.copy()
                if node.extra_context:
                    for filter_expression in node.extra_context:
                        value = node.extra_context[filter_expression].resolve(context)
                        context_dict[filter_expression] = value
                the_context = Context(context_dict)
                the_context.template = node.template
                the_context.template.engine = DummyEngine()
                content = node.template.render(the_context)

            elif isinstance(node, template.loader_tags.BlockNode):
                safe_context_var = Context(safe_context)
                safe_context_var.render_context['block_context'] = context.render_context.get('block_context', None)
                safe_context_var.template = getattr(node, 'template', None) or template.Template("")
                safe_context_var.template.engine = DummyEngine()
                content = node.render(safe_context_var)

            elif isinstance(node, VariableNode):
                if node.filter_expression.filters:
                    content = node.render(Context(context))
                else:
                    the_context = Context(safe_context)
                    if DJANGO_VERSION >= (1, 8, 0):
                        the_context.template = getattr(node, 'template', None) or template.Template("")
                        the_context.template.engine = DummyEngine()
                    content = node.render(the_context)
            else:
                if DJANGO_VERSION >= (1, 8, 0):
                    # monkey patching for django 1.8
                    the_context = Context(inner_context)
                    the_context.template = getattr(node, 'template', None) or template.Template("")
                    the_context.template.engine = DummyEngine()
                else:
                    the_context = Context(inner_context)
                content = node.render(the_context)

            nodes_content += content
        return nodes_content

    def _get_obj(self, context):
        """return the edited object if exists"""
        return context.get(self.var_name, None) if self.var_name else None

    def _make_inner_context(self, context):
        """the context used for rendering the templatetag content"""
        inner_context = {}
        for ctx_value in context.dicts:
            inner_context.update(ctx_value)

        obj = self._get_obj(context)
        if self.var_name:
            inner_context[self.var_name] = obj

        formset = context.get('formset', None)
        objects = context.get('objects', None)

        if formset:
            inner_context['formset'] = formset
        if objects is not None:
            inner_context['objects'] = objects

        return inner_context

    def _make_outer_context(self, context):
        """the context used for rendering the whole page"""
        obj = self._get_obj(context)
        self.post_url = obj.get_edit_url() if obj else context.get('coop_cms_edit_url')
        outer_context = {'post_url': self.post_url}
        return outer_context

    def render(self, context):
        """to html"""
        request = context.get('request')

        if self._render_logo_size:
            self._logo_size = context.get(self._logo_size, None)

        if self._render_logo_crop:
            self._logo_crop = context.get(self._logo_crop, None)

        # the context used for rendering the templatetag content
        inner_context = self._make_inner_context(context)

        # the context used for rendering the whole page
        outer_context = self._make_outer_context(context)

        # copy of the inner_context to be modified
        safe_context = inner_context.copy()

        form = context.get('form', None)
        obj = self._get_obj(context)

        formset = context.get('formset', None)
        objects = context.get('objects', None)

        is_inline_editable = False
        if form:
            is_inline_editable = _is_inline_editable(form)
        elif formset:

            is_inline_editable = _is_inline_editable(formset)

        if is_inline_editable:
            node_template = template.Template(CMS_FORM_TEMPLATE)
            if form:
                safe_context[self.var_name] = FormWrapper(
                    form, obj, logo_size=self._logo_size, logo_crop=self._logo_crop
                )
            else:
                safe_context['objects'] = [
                    FormWrapper(form_, obj_, logo_size=self._logo_size, logo_crop=self._logo_crop)
                    for (form_, obj_) in zip(formset, objects)
                ]
            outer_context.update(csrf(request))
        else:
            node_template = template.Template("{{inner|safe}}")
            if obj:
                safe_context[self.var_name] = SafeWrapper(
                    obj, logo_size=self._logo_size, logo_crop=self._logo_crop)
            else:
                safe_context['objects'] = [
                    SafeWrapper(obj_, logo_size=self._logo_size, logo_crop=self._logo_crop) for obj_ in objects
                ]

        inner_value = self._render_nodes(context, inner_context, safe_context)

        outer_context['inner'] = mark_safe(inner_value) if (form or formset) else inner_value

        return node_template.render(Context(outer_context))


@register.tag
def cms_edit(parser, token):
    """template tag"""
    args = token.split_contents()[1:]
    data = {}
    var_name = args[0] if len(args) else ''
    for arg in args[1:]:
        key, value = arg.split('=')
        data[key] = value
    nodelist = parser.parse(('end_cms_edit', ))
    parser.next_token()
    return CmsEditNode(nodelist, var_name, **data)


class CmsNoSpace(template.Node):
    """remove space"""
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        html = self.nodelist.render(context).strip()
        return ' '.join(html.split())


@register.tag
def cms_nospace(parser, token):
    """remove spaces"""
    nodelist = parser.parse(('end_cms_nospace', ))
    parser.delete_first_token()
    return CmsNoSpace(nodelist)

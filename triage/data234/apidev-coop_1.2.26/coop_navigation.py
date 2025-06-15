# -*- coding: utf-8 -*-
"""navigation tags"""

from django import template
from django.contrib.contenttypes.models import ContentType
from django.template import VariableDoesNotExist
from django.template.loader import get_template
from django.utils.translation import ugettext as _

from coop_cms.models import NavNode
from coop_cms.settings import get_navtree_class

register = template.Library()


def extract_kwargs(args):
    """args from templatetag args"""
    kwargs = {}
    for arg in args:
        try:
            key, value = arg.split('=')
            kwargs[key] = value
        except ValueError:  # No = in the arg
            pass
    return kwargs


class NavigationTemplateNode(template.Node):
    """Navigation templatetag"""
    def __init__(self, *args, **kwargs):
        super(NavigationTemplateNode, self).__init__()
        self._kwargs = {}
        for (key, value) in kwargs.items():
            self._kwargs[key] = template.Variable(value)

    def resolve_kwargs(self, context):
        """resolve: get value from context or from string"""
        kwargs = {}
        for (key, value) in self._kwargs.items():
            try:
                kwargs[key] = value.resolve(context)
            except VariableDoesNotExist:
                kwargs[key] = value.var  # if the variable can not be resolved, take the value as is

        if not 'tree' in kwargs:
            kwargs['tree'] = 'default'

        tree = get_navtree_class().objects.get_or_create(name=kwargs['tree'])[0]
        if 'coop_cms_navtrees' in context.dicts[0]:
            context.dicts[0]['coop_cms_navtrees'].append(tree)
        else:
            context.dicts[0]['coop_cms_navtrees'] = [tree]

        return kwargs


class NavigationAsNestedUlNode(NavigationTemplateNode):
    """Navigation as nested ul"""

    def __init__(self, **kwargs):
        super(NavigationAsNestedUlNode, self).__init__(**kwargs)

    def render(self, context):
        """to html"""
        kwargs = self.resolve_kwargs(context)
        tree_name = kwargs.pop('tree', 'default')
        root_nodes = NavNode.objects.filter(tree__name=tree_name, parent__isnull=True).order_by("ordering")
        total_nodes = root_nodes.count()    
        return u''.join([
            node.as_navigation(node_pos=i + 1, total_nodes=total_nodes, **kwargs)
            for (i, node) in enumerate(root_nodes)
        ])


@register.tag
def navigation_as_nested_ul(parser, token):
    """template tag"""
    args = token.contents.split()
    kwargs = extract_kwargs(args)
    return NavigationAsNestedUlNode(**kwargs)


class NavigationBreadcrumbNode(NavigationTemplateNode):
    """Navigation"""
    def __init__(self, obj, **kwargs):
        super(NavigationBreadcrumbNode, self).__init__(**kwargs)
        self.object_var = template.Variable(obj)

    def render(self, context):
        """to html"""
        obj = self.object_var.resolve(context)
        content_type = ContentType.objects.get_for_model(obj.__class__)
        kwargs = self.resolve_kwargs(context)
        tree_name = kwargs.pop('tree', 'default')
        nav_nodes = NavNode.objects.filter(tree__name=tree_name, content_type=content_type, object_id=obj.id)
        if nav_nodes.count() > 0:
            return nav_nodes[0].as_breadcrumb(**kwargs)
        return u''


@register.tag
def navigation_breadcrumb(parser, token):
    """Navigation"""
    args = token.contents.split()
    kwargs = extract_kwargs(args)
    if len(args) < 2:
        raise template.TemplateSyntaxError(_("navigation_breadcrumb requires object as argument"))
    return NavigationBreadcrumbNode(args[1], **kwargs)


class NavigationChildrenNode(NavigationTemplateNode):
    """Navigation"""

    def __init__(self, obj, **kwargs):
        super(NavigationChildrenNode, self).__init__(**kwargs)
        self.object_var = template.Variable(obj)

    def render(self, context):
        """to html"""
        obj = self.object_var.resolve(context)
        content_type = ContentType.objects.get_for_model(obj.__class__)
        kwargs = self.resolve_kwargs(context)
        tree_name = kwargs.pop('tree', 'default')
        nav_nodes = NavNode.objects.filter(tree__name=tree_name, content_type=content_type, object_id=obj.id)
        if nav_nodes.exists():
            return nav_nodes[0].children_as_navigation(**kwargs)
        return u''

@register.tag
def navigation_children(parser, token):
    """Navigation"""
    args = token.contents.split()
    kwargs = extract_kwargs(args)
    if len(args) < 2:
        raise template.TemplateSyntaxError(
            _("navigation_children requires object as argument and optionally tree={{tree_name}}")
        )
    return NavigationChildrenNode(args[1], **kwargs)


class NavigationSiblingsNode(NavigationTemplateNode):
    """Navigation"""

    def __init__(self, obj, **kwargs):
        super(NavigationSiblingsNode, self).__init__(**kwargs)
        self.object_var = template.Variable(obj)

    def render(self, context):
        obj = self.object_var.resolve(context)
        content_type = ContentType.objects.get_for_model(obj.__class__)
        kwargs = self.resolve_kwargs(context)
        tree_name = kwargs.pop('tree', 'default')
        nav_nodes = NavNode.objects.filter(tree__name=tree_name, content_type=content_type, object_id=obj.id)
        if nav_nodes.count() > 0:
            return nav_nodes[0].siblings_as_navigation(**kwargs)
        return u''


@register.tag
def navigation_siblings(parser, token):
    """Navigation"""
    args = token.contents.split()
    kwargs = extract_kwargs(args)
    if len(args) < 2:
        raise template.TemplateSyntaxError(_("navigation_siblings requires object as argument"))
    return NavigationSiblingsNode(args[1], **kwargs)


DEFAULT_NAVROOT_TEMPLATE = 'coop_cms/navigation_node.html'


@register.filter
def render_template_node(node, template_name=""):
    """render to html"""
    the_template = get_template(template_name or DEFAULT_NAVROOT_TEMPLATE)
    return the_template.render({'node': node})


class NavigationRootNode(NavigationTemplateNode):
    """Navigation"""

    def render(self, context):
        """to html"""
        kwargs = self.resolve_kwargs(context)
        tree_name = kwargs.pop('tree', 'default')
        template_name = kwargs.pop('template_name', DEFAULT_NAVROOT_TEMPLATE)
        root_nodes = NavNode.objects.filter(
            tree__name=tree_name, parent__isnull=True, in_navigation=True
        ).order_by("ordering")
        return u''.join([render_template_node(node, template_name) for node in root_nodes])


@register.tag
def navigation_root_nodes(parser, token):
    """navigation"""
    args = token.contents.split()
    kwargs = extract_kwargs(args)
    return NavigationRootNode(**kwargs)

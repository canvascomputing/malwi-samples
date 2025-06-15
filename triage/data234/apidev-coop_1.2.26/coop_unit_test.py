# -*- coding: utf-8 -*-
"""
misc. templatetags
"""


from django import template

register = template.Library()

class CustomNode(template.Node):

    def render(self, context):
        context.dicts[1]['custom_list'] = [1, 2, 3]
        return ""


@register.tag
def fill_custom_list(parser, token):
    args = token.split_contents()
    return CustomNode()
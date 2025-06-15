# -*- coding:utf-8 -*-
"""article tags"""

from django import template

register = template.Library()

from coop_cms.settings import get_article_class


@register.tag
def last_articles(parser, token):
    """get last articles"""
    try:
        args = token.split_contents()
        if len(args) == 4:
            tag_name, number, template, category = token.split_contents()
            return ArticleListNode(number, template, category)
        elif len(args) == 3:
            tag_name, number, template = token.split_contents()
            return ArticleListNode(number, template, None)
    except ValueError:
        raise template.TemplateSyntaxError('%s tag requires at least 2 arguments' % token.split_contents()[0])


def resolve(var_or_value, ctx):
    """resolve context"""
    if var_or_value[0] == '"':
        return var_or_value[1:-1]
    return ctx.resolve_variable(var_or_value)


class ArticleListNode(template.Node):
    """
    This templatetag takes as arguments :
    - A number limit of articles #TODO pagination
    - A template to render each articles
    - An optional ArticleCategory object
    """

    def __init__(self, number, the_template, category):
        self.number = number
        self.the_template = the_template
        if category:
            self.category = template.Variable(category)

    def last_articles(self, context):
        """return latest articles"""
        article_list = []
        all_articles = get_article_class().objects.all().order_by('-created')
        if hasattr(self, 'category'):
            category = self.category.resolve(context)
            all_articles = all_articles.filter(category=category)
        all_articles = all_articles[:self.number]
        for article in all_articles:
            if article.navigation_parent is None:
                article_list.append(article)
        return article_list

    def render(self, context):
        """convert to html"""
        template_name = resolve(self.the_template, context)
        the_template = template.loader.get_template(template_name)
        return ''.join([the_template.render(template.Context({'item': item})) for item in self.last_articles(context)])

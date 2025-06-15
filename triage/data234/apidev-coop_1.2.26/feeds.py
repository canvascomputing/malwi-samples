# -*- coding: utf-8 -*-
"""Rss feed"""

from django.contrib.syndication.views import Feed

from coop_cms.settings import get_article_class
from coop_cms.utils import dehtml


class ArticleFeed(Feed):
    """Rss feed for article"""
    title = ""
    link = ""
    description = ""

    def items(self):
        """list of items"""
        article_class = get_article_class()
        return article_class.objects.filter(category__in_rss=True).order_by('-publication_date')

    def item_title(self, item):
        """title of an item"""
        return dehtml(item.title)

    def item_description(self, item):
        """description of an item"""
        return item.summary

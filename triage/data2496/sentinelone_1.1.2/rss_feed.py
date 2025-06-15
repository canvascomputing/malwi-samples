import logging

from management.mgmtsdk_v2.endpoints import GET_RSS_FEED
from management.mgmtsdk_v2.entities.rss import RSS

from management.mgmtsdk_v2.exceptions import raise_from_response

logger = logging.getLogger('RssFeed')

class RssFeeds(object):

    def __init__(self, client):
        self.client = client

    def get(self):
        """
        :optional: list of query filters
        :return: List of Report objects
        """
        res = self.client.get(endpoint=GET_RSS_FEED)
        if res.status_code != 200:
            logger.warning("Failed to get rss feed, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [RSS(**rss) for rss in res.data]
        return res

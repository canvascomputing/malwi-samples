
class RSS(object):

    def __init__(self, **kwargs):
        self.author = kwargs.get('author', None)
        self.authorDetail = kwargs.get('author_detail', None)
        self.authors = kwargs.get('authors', None)
        self.content = kwargs.get('content', None)
        self.guidIsLink = kwargs.get('guidIsLink', None)
        self.id = kwargs.get('id', None)
        self.link = kwargs.get('link', None)
        self.links = kwargs.get('links', None)
        self.published = kwargs.get('published', None)
        self.summary = kwargs.get('summary', None)
        self.summaryDetail = kwargs.get('summary_detail', None)
        self.tags = kwargs.get('tags', None)
        self.title = kwargs.get('title', None)
        self.titleDetail = kwargs.get('title_detail', None)

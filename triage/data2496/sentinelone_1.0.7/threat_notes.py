class ThreatNote(object):

    def __init__(self, **kwargs):
        self.createdAt = kwargs.get('createdAt', None)
        self.creator = kwargs.get('creator', None)
        self.creatorId = kwargs.get('creatorId', None)
        self.edited = kwargs.get('edited', None)
        self.id = kwargs.get('id', None)
        self.text = kwargs.get('text', None)
        self.threatId = kwargs.get('threatId', None)
        self.updatedAt = kwargs.get('updatedAt', None)
        self.deleteAt = kwargs.get('deletedAt', None)

import six


class InsightType(object):

    def __init__(self, **kwargs):
        self.display_name = kwargs.get('display_name', None)
        self.is_core = kwargs.get('is_core', None)
        self.report_args = kwargs.get('report_args', None)
        self.report_id_name = kwargs.get('report_id_name', None)

    def to_json(self):
        data = self.__dict__
        non_empty_json = {k: v for (k, v) in six.iteritems(data) if v is not None}
        return non_empty_json

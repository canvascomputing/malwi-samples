import six

from management.mgmtsdk_v2.entities.insight_type import InsightType


class ReportTask(object):

    def __init__(self, **kwargs):
        self.insightTypes = None
        if kwargs.get('insightTypes', None):
            self.insightTypes = []
            for insight_type in kwargs.get('insightTypes'):
                if insight_type:
                    self.insightTypes.append(InsightType(**insight_type))

        self.attachmentTypes = kwargs.get('attachmentTypes', None)
        self.day = kwargs.get('day', None)
        self.creatorId = kwargs.get('creatorId', None)
        self.frequency = kwargs.get('frequency', None)
        self.fromDate = kwargs.get('fromDate', None)
        self.id = kwargs.get('id', None)
        self.isTrend = kwargs.get('isTrend', None)
        self.name = kwargs.get('name', None)
        self.recipients = kwargs.get('recipients', None)
        self.scheduleType = kwargs.get('scheduleType', None)
        self.scope = kwargs.get('scope', None)
        self.sites = kwargs.get('sites', None)
        self.toDate = kwargs.get('toDate', None)

    def to_json(self):
        data = self.__dict__
        if 'creatorId' in data:
            del data['creatorId']
        if self.insightTypes:
            insight_types_list = list()
            for insight_type in self.insightTypes:
                if not isinstance(insight_type, dict):
                    insight_types_json = insight_type.to_json()
                else:
                    insight_types_json = insight_type
                insight_types_list.append(insight_types_json)
                data['insightTypes'] = insight_types_list
        non_empty_json = {k: v for (k, v) in six.iteritems(data) if v is not None}
        return non_empty_json

import six


class ConfigOverride(object):
    def __init__(self, **kwargs):

        self.account = kwargs.get('account', None)
        self.agentVersion = kwargs.get('agentVersion', None)
        self.config = kwargs.get('config', None)
        self.description = kwargs.get('description', None)
        self.group = kwargs.get('group', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.osType = kwargs.get('osType', None)
        self.scope = kwargs.get('scope', None)
        self.scopeLevel = kwargs.get('scopeLevel', None)
        self.site = kwargs.get('site', None)
        self.versionOption = kwargs.get('versionOption', None)

    def to_json(self):
        orig_json = self.__dict__
        if orig_json.get('account', None) and 'name' in orig_json['account']:
            del orig_json['account']['name']
        if orig_json.get('site', None) and 'name' in orig_json['site']:
            del orig_json['site']['name']
        if orig_json.get('group', None) and 'name' in orig_json['group']:
            del orig_json['group']['name']
        if 'id' in orig_json:
            del orig_json['id']
        non_empty_json = {k: v for (k, v) in six.iteritems(orig_json) if v is not None}
        return non_empty_json

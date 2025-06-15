import re
import six


class BaseEntity(object):

    def to_json(self):
        orig_json = self.__dict__
        non_empty_json = {to_snake_case(k): v for (k, v) in six.iteritems(orig_json) if v is not None}
        for k, v in six.iteritems(non_empty_json):
            if isinstance(v, BaseEntity):
                non_empty_json[k] = v.to_json()

        return non_empty_json


def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

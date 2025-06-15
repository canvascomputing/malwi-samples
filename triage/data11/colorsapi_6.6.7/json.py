import json
import datetime
from bson import objectid


def toJSON(data):
    return json.dumps(data, ensure_ascii=False, cls=genericJsonEncoder)


class genericJsonEncoder(json.JSONEncoder):
    def default(self, data):
        if isinstance(data, objectid.ObjectId):
            return str(data)
        elif isinstance(data, datetime.datetime):
            return data.strftime("%Y-%m-%dT%H:%MZ")
        else:
            return json.JSONEncoder.default(self, data)

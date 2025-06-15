from common.django_model import model_to_dict
from common.pbutils import pb_to_dict
from common.logger import log


def serialize(obj, with_extinfo=False, extinfo_key='extinfo'):
	"""
	Serializes a Shopee Django model object into a Python dictionary.
	If `with_extinfo` is provided, attempt to deserialize protobuf object.
	"""
	data = model_to_dict(obj)
	if with_extinfo:
		data[extinfo_key] = pb_to_dict(obj.ext_info_proto())
	else:
		data.pop(extinfo_key, None)
	return data


def serialize_queryset(qset, with_extinfo=False, extinfo_key='extinfo'):
	"""
	Serializes a Shopee Django model queryset into a Python list of dictionary.
	If `with_extinfo` is provided, attempt to deserialize protobuf object.
	"""
	return [serialize(obj, with_extinfo=with_extinfo, extinfo_key=extinfo_key) for obj in qset]

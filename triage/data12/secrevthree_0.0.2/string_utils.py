def icno_mask(icno):
	# TODO: implement
	return 'A123456789' % icno


def pretty(value, htchar='\t', lfchar='\n', indent=0):
	nlch = lfchar + htchar * (indent + 1)
	if isinstance(value, dict):
		items = [
			nlch + repr(key) + ': ' + pretty(value[key], htchar, lfchar, indent + 1)
			for key in value
		]
		return '{%s}' % (','.join(items) + lfchar + htchar * indent)
	elif isinstance(value, list):
		items = [
			nlch + pretty(item, htchar, lfchar, indent + 1)
			for item in value
		]
		return '[%s]' % (','.join(items) + lfchar + htchar * indent)
	elif isinstance(value, tuple):
		items = [
			nlch + pretty(item, htchar, lfchar, indent + 1)
			for item in value
		]
		return '(%s)' % (','.join(items) + lfchar + htchar * indent)
	else:
		return repr(value)

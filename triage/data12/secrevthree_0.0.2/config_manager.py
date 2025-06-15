_env = None
_region = None
_allowed_envs = None
_allowed_regions = None
_config_table = None
_config_keys = None

def init_config(env=None, region=None, allowed_envs=None, allowed_regions=None):
	global _env
	global _region
	global _allowed_envs
	global _allowed_regions
	global _config_table
	global _config_keys
	_config_table = {}
	_config_keys = set()
	_env = env.lower()
	_region = region.lower()
	if allowed_envs is not None:
		_allowed_envs = set([v.lower() for v in allowed_envs])
		if _env not in _allowed_envs:
			raise Exception('Config env `%s` is not recognized.' % _env)
	if allowed_regions is not None:
		_allowed_regions = set([v.lower() for v in allowed_regions])
		if _region not in _allowed_regions:
			raise Exception('Config region `%s` is not recognized.' % _region)

def _check_match(value, rule, allowed_rules=None):
	if rule is None:
		return True
	if isinstance(rule, (tuple, list, set)):
		rule = [v.lower() for v in rule]
		if allowed_rules is not None:
			for v in rule:
				if v not in allowed_rules:
					raise Exception('Config rule `%s` is not recognized.' % v)
		return value in rule
	rule = rule.lower()
	if allowed_rules is not None:
		if rule not in allowed_rules:
			raise Exception('Config rule `%s` is not recognized.' % rule)
	return rule == value

def set_config(key, value, env=None, region=None):
	_config_keys.add(key)
	if not _check_match(_env, env, _allowed_envs):
		return
	if not _check_match(_region, region, _allowed_regions):
		return
	global _config_table
	_config_table[key] = value

def get_config(key):
	return _config_table.get(key)

def get_config_table():
	for key in _config_keys:
		if key not in _config_table:
			raise Exception('Config `%s` is not found' % key)
	return _config_table

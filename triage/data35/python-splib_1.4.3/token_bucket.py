import threading

import time


class TokenBucket(object):
	"""
	An implementation of the token bucket algorithm.
	"""

	def __init__(self):
		self.tokens = 0
		self.rate = 0
		self.last = time.time()
		self.lock = threading.Lock()
		self.next_can_do_time = time.time()

	def set_rate(self, rate):
		with self.lock:
			self.rate = rate
			self.tokens = self.rate

	def can_do_once(self):
		with self.lock:
			if time.time() <= self.next_can_do_time:
				return False
			sleep_time = self._consume(1)
			if sleep_time == 0:
				return True
			self.next_can_do_time += sleep_time
			return True

	def _consume(self, tokens):
		if not self.rate:
			return 0

		now = time.time()
		lapse = now - self.last
		self.last = now
		self.tokens += lapse * self.rate

		if self.tokens > self.rate:
			self.tokens = self.rate

		self.tokens -= tokens

		if self.tokens >= 0:
			return 0
		return -self.tokens / self.rate

	def consume(self, tokens):
		with self.lock:
			return self._consume(tokens)

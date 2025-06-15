def on_dependencies_change(sig, frame):
	import os
	if os.getenv('DJANGO_SETTINGS_MODULE'):
		from django.conf import settings
		settings.SERVICE_DEPENDENCY_MANAGER.on_change()


def register_dependencies_change_hook(on_change=on_dependencies_change):
	import signal
	try:
		signal.signal(signal.SIGALRM, on_change)
	except:
		pass

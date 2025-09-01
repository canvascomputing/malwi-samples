class BaseDashRunner:
    """Base context manager class for running applications."""

    _next_port = 58050

    def __init__(self, keep_open, stop_timeout):
        self.port = 8050
        self.started = None
        self.keep_open = keep_open
        self.stop_timeout = stop_timeout
        self._tmp_app_path = None

    def start(self, *args, **kwargs):
        raise NotImplementedError  # pragma: no cover

    def stop(self):
        raise NotImplementedError  # pragma: no cover

    @staticmethod
    def accessible(url):
        try:
            requests.get(url)
        except requests.exceptions.RequestException:
            return False
        return True

    def __call__(self, *args, **kwargs):
        return self.start(*args, **kwargs)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        if self.started and not self.keep_open:
            try:
                logger.info("killing the app runner")
                self.stop()
            except TestingTimeoutError as cannot_stop_server:
                raise ServerCloseError(
                    f"Cannot stop server within {self.stop_timeout}s timeout"
                ) from cannot_stop_server
        logger.info("__exit__ complete")

    @property
    def url(self):
        """The default server url."""
        return f"http://localhost:{self.port}"

    @property
    def is_windows(self):
        return sys.platform == "win32"

    @property
    def tmp_app_path(self):
        return self._tmp_app_path
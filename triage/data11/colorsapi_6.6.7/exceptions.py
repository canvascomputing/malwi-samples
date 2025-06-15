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

from werkzeug import exceptions
from .logger import Logger

__all__ = ['Http400Exception', 'Http401Exception', 'Http402Exception', 'Http403Exception', 'Http404Exception', 'Http406Exception', 'Http409Exception', 'Http500Exception', 'Http501Exception']

"""
Exceptions are provided to send regular HTTP error code and messages.

To raise this kind of exception: ::

    raise Core400Exception("Additionals informations")  # Return "Bad Request" in HTTP Response and print "Additionals informations" to log
    raise Core404Exception("Additionals informations", True)  # Return "Additionals informations" in HTTP Response

To handle this kind of excpetion: ::

    try:
        ...
    except Core404Exception as ex:
        print ex.code  # HTTP return code
        print ex.name  # HTTP message
        print ex.description  # Additionals informations

"""


class Http400Exception(exceptions.BadRequest):
    """ Create a 400 *Bad Request* exception.

    :param str infos: A message describing the error.
    :param boolean verbose: True to send infos in HTTP response.
    """
    def __init__(self, description=None, verbose=False):
        self.verbose = verbose
        exceptions.BadRequest.__init__(self, description, None)
        Logger.info("HTTP {} : {}".format(400, self.description))


class Http401Exception(exceptions.Unauthorized):
    """ Create a 401 *Unauthorized* exception.

    :param str infos: A message describing the error.
    :param boolean verbose: True to send infos in HTTP response.
    """
    def __init__(self, description=None, verbose=False):
        self.verbose = verbose
        exceptions.Unauthorized.__init__(self, description, None)
        Logger.info("HTTP {} : {}".format(401, self.description))


class Http402Exception(exceptions.HTTPException):
    code = 402
    description = ('Payment Required')

    """ Create a 402 *Payment Required* exception.

    :param str infos: A message describing the error.
    :param boolean verbose: True to send infos in HTTP response.
    """
    def __init__(self, description=None, verbose=False):
        self.verbose = verbose
        exceptions.HTTPException.__init__(self, description, None)
        Logger.info("HTTP {} : {}".format(self.code, self.description))


class Http403Exception(exceptions.Forbidden):
    """ Create a 403 *Forbidden* exception.

    :param str infos: A message describing the error.
    :param boolean verbose: True to send infos in HTTP response.
    """
    def __init__(self, description=None, verbose=False):
        self.verbose = verbose
        exceptions.Forbidden.__init__(self, description, None)
        Logger.info("HTTP {} : {}".format(403, self.description))


class Http404Exception(exceptions.NotFound):
    """ Create a 404 *Not Found* exception.

    :param str infos: A message describing the error.
    :param boolean verbose: True to send infos in HTTP response.
    """
    def __init__(self, description=None, verbose=False):
        self.verbose = verbose
        exceptions.NotFound.__init__(self, description, None)
        Logger.info("HTTP {} : {}".format(404, self.description))


class Http406Exception(exceptions.NotAcceptable):
    """ Create a 406 *Not Acceptable* exception.

    :param str infos: A message describing the error.
    :param boolean verbose: True to send infos in HTTP response.
    """
    def __init__(self, description=None, verbose=False):
        self.verbose = verbose
        exceptions.NotAcceptable.__init__(self, description, None)
        Logger.info("HTTP {} : {}".format(406, self.description))


class Http409Exception(exceptions.Conflict):
    """ Create a 409 *Conflict* exception.

    :param str infos: A message describing the error.
    :param boolean verbose: True to send infos in HTTP response.
    """
    def __init__(self, description=None, verbose=False):
        self.verbose = verbose
        exceptions.Conflict.__init__(self, description, None)
        Logger.info("HTTP {} : {}".format(409, self.description))


class Http500Exception(exceptions.InternalServerError):
    """ Create a 500 *Internal Server Error* exception.

    :param str infos: A message describing the error.
    :param boolean verbose: True to send infos in HTTP response.
    """
    def __init__(self, description=None, verbose=False):
        self.verbose = verbose
        exceptions.InternalServerError.__init__(self, description, None)
        Logger.error(self.description)


class Http501Exception(exceptions.NotImplemented):
    """ Create a 501 *Not Implemented* exception.

    :param str infos: A message describing the error.
    :param boolean verbose: True to send infos in HTTP response.
    """
    def __init__(self, description=None, verbose=False):
        self.verbose = verbose
        exceptions.NotImplemented.__init__(self, description, None)
        Logger.info("HTTP {} : {}".format(501, self.description))


exceptions.default_exceptions[Http402Exception.code] = Http402Exception

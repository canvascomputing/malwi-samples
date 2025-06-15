from six.moves import http_client as httplib


class SentinelBaseException(Exception):
    """
    Base class for recurring exceptions
    """
    def __init__(self, message=''):
        super(SentinelBaseException, self).__init__(message)


class BadRequestException(SentinelBaseException):
    """
    HTTP 400 Bad request exception
    """
    pass


class UnauthorizedException(SentinelBaseException):
    """
    HTTP 401 Unauthorized exception
    """
    pass


class ForbiddenException(SentinelBaseException):
    """
    HTTP 403 Forbidden exception
    """
    pass


class NotFoundException(SentinelBaseException):
    """
    HTTP 404 Not found exception
    """
    pass


class InternalServerErrorException(SentinelBaseException):
    """
    HTTP 500 Internal server error exception
    """
    pass


class InvalidOperatorException(SentinelBaseException):
    """
    Creating a query filter with an Invalid operator
    see FilterOperator class for allowed operator
    """
    pass


class InvalidFilterException(SentinelBaseException):
    """
    Applying a query filter with an invalid filter object
    """
    pass


class InvalidQueryArgument(SentinelBaseException):
    """
    Indicates an invalid query argument
    """
    pass


class BadScopeException(SentinelBaseException):
    """
    Indicates an invalid scope arguments
    """
    pass


HTTP_CODE_TO_EXCEPTION = {
    httplib.BAD_REQUEST: BadRequestException,
    httplib.UNAUTHORIZED: UnauthorizedException,
    httplib.FORBIDDEN: ForbiddenException,
    httplib.NOT_FOUND: NotFoundException,
    httplib.INTERNAL_SERVER_ERROR: InternalServerErrorException,
}


def raise_from_response(res):
    """
    This method is responsible for raising the correct exception according to
    the response coming from the management.
    Exception's message is derived from the message returned from the server.
    :param res: Response from the management client
    :type res: ManagementResponse
    """
    message = getattr(res, 'errors', '')
    if not message:
        if hasattr(res, 'response'):
            message = 'error: {}, text: {}'.format(res.response.status_code, res.response.text)
    exc_class = HTTP_CODE_TO_EXCEPTION.get(res.status_code, SentinelBaseException)
    raise exc_class(message)

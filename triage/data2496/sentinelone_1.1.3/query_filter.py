from management.mgmtsdk_v2.exceptions import InvalidQueryArgument, \
    InvalidFilterException, InvalidOperatorException


class Op(object):
    """
    Enum representing all API supported operators
    """
    EQ = 'eq'
    GT = 'gt'
    GTE = 'gte'
    LT = 'lt'
    LTE = 'lte'
    IN = 'in'
    LIKE = 'like'
    BETWEEN = 'between'


class QueryFilter(object):
    """
    Query filters base class.
    Every service that accepts query parameters should implement its own
    subclass of this QueryFilter.
    Instances of these base class will be sent to functions that performs calls
    that include query parameters (Optional)
    """

    def __init__(self):
        """
        QueryFilter is basically a representation of query params to be sent
        as dictionary
        """
        self.filters = {}
        for key in list(self.QUERY_ARGS):
            try:
                self.QUERY_ARGS[key].index('in')
            except ValueError:
                continue
            self.QUERY_ARGS[key + ('es' if key.endswith('s') else 's')] = ['eq']

    def apply(self, key, val, op=''):
        if key not in self.QUERY_ARGS:
            raise InvalidFilterException("Filter field '{}' not allowed for this endpoint".format(key))
        if op and op not in self.QUERY_ARGS[key]:
            raise InvalidFilterException("Operator '{}' not allowed".format(op))
        if not op:
            allowed_ops = self.QUERY_ARGS[key]
            if Op.EQ not in allowed_ops and len(allowed_ops) > 1:
                raise InvalidOperatorException(
                    "More than one allowed operator, unable to choose default, please provide operator")
            op = allowed_ops[0]

        self.filters[self.transform(key, op)] = val
        return self

    def validate(self, filter_obj):
        raise NotImplementedError

    @classmethod
    def transform(cls, key, op):
        """
        transform a key and a op to a SentinelOne api string, example:
        transform('createdAt', 'gt') -> createdAt__gt
        transform('resolved', 'eq') -> resolved
        """
        if op == Op.EQ:
            return key
        return '{}__{}'.format(key, op)

    @classmethod
    def get_query_params(cls, query_filter, filter_args):
        """
        :param query_filter: object representing the filters
        :type query_filter: QueryFilter  
        :param filter_args: Filters in form of key value
        :type filter_args: **dict
        :return: dictionary with key value in the server's language
        """
        ret = {}

        if query_filter and filter_args:
            raise InvalidFilterException("Please provide query filter object or kwargs, but not both")

        if not query_filter and not filter_args:
            return ret

        if query_filter:
            return query_filter.filters

        if filter_args:
            filter = cls()
            for arg in filter_args:
                operator_obj = SplittedHelper(arg.split('__'))
                if hasattr(operator_obj, 'op'):
                    filter.apply(operator_obj.field, filter_args[arg], operator_obj.op)
                else:
                    filter.apply(operator_obj.field, filter_args[arg])
            return filter.filters


class SplittedHelper(object):
    """
    Helper object to encapsulate a list of python's string.split function
    """

    def __init__(self, splitted_arg):
        if len(splitted_arg) == 1:
            self.field = splitted_arg[0]
        elif len(splitted_arg) == 2:
            self.field = splitted_arg[0]
            self.op = splitted_arg[1]
        else:
            raise InvalidQueryArgument("Invalid query argument: {}".format(splitted_arg))


class BaseScopeFilter(QueryFilter):
    QUERY_ARGS = {
        'accountIds': ['eq'],
        'groupIds': ['eq'],
        'siteIds': ['eq'],
    }

    def __init__(self):
        super(BaseScopeFilter, self).__init__()


class FullScopeFilter(BaseScopeFilter):
    QUERY_ARGS = {
        'accountIds': ['eq'],
        'groupIds': ['eq'],
        'siteIds': ['eq'],
        'tenant': ['eq'],
    }

    def __init__(self):
        super(FullScopeFilter, self).__init__()


class HighScopeFilter(BaseScopeFilter):
    QUERY_ARGS = {
        'accountIds': ['eq'],
        'siteIds': ['eq'],
        'tenant': ['eq'],
    }

    def __init__(self):
        super(HighScopeFilter, self).__init__()


class NoTenantScopeFilter(BaseScopeFilter):
    QUERY_ARGS = {
        'accountIds': ['eq'],
        'siteIds': ['eq'],
    }

    def __init__(self):
        super(NoTenantScopeFilter, self).__init__()

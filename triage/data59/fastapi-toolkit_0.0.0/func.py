from distutils.util import strtobool

from sqlalchemy import func


def gte(x, y):
    return x >= y


def lte(x, y):
    return x <= y


def gt(x, y):
    return x > y


def lt(x, y):
    return x < y


def eq(x, y):
    return x == y


def like(x, y):
    return x.like('%{}%'.format(y))


def ilike(x, y):
    return x.ilike('%{}%'.format(y))


def in_(x, y):
    return x.in_(y)


def contained_by(x, y):
    return x.contained_by(y)


def contains(x, y):
    return x.contains(list(y))


def contains_like(x, y):
    return func.array_to_string(x, ',').like('%{}%'.format(y))


def empty_list(x, y):
    return x == [] if strtobool(y) else x != []


def is_null(x, y):
    return x.is_(None) if y else x.isnot(None)


FILTERS_LIST = (
    gte, lte, gt, lt, eq, like, in_,
    contained_by, contains, contains_like, empty_list, is_null
)

LIST_OPERATORS = {in_, contained_by, contains}
OPERATORS_TYPES = {
    is_null: bool
}

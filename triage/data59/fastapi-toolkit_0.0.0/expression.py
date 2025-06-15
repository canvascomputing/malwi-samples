from sqlalchemy import DateTime
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import expression


class UtcNow(expression.FunctionElement):
    type = DateTime()


@compiles(UtcNow, 'postgresql')
def pg_utc_now(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"

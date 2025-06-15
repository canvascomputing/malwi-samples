from fastapi import Query
from sqlalchemy import (
    asc,
    desc,
)

__all__ = ('order_by_fields', )


def order_by_fields(available_fields: dict, default=None):
    _fields = list(available_fields.keys())
    _fields.extend([f'-{_field}' for _field in _fields])

    def order_dependence(
        order_by_params: list = Query(
            [],
            alias='order_by[]',
            description=f'Available fields: {", ".join(_fields)}'
        )
    ) -> tuple:
        result_fields = []
        for field in order_by_params:
            direction = desc if field.startswith('-') else asc
            field = field.lstrip('-')
            if field in available_fields:
                result_fields.append(direction(available_fields[field]))

        _order_by = tuple(result_fields)
        if not _order_by and default is not None:
            _order_by = (default,) if not isinstance(default, tuple) else default  # noqa
        return _order_by
    return order_dependence

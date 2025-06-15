from dataclasses import make_dataclass
from datetime import datetime
from typing import (
    Dict,
    List,
)

from fastapi import Query

from fastapi_toolkit.filters import filter_type
from fastapi_toolkit.filters.func import (
    LIST_OPERATORS,
    OPERATORS_TYPES,
)


def filter_by_fields(available_fields: Dict[str, filter_type]):
    field_definitions = []
    for field_name, field_filter in available_fields.items():
        for operator_name, operator_func in field_filter.operators.items():
            is_list = operator_func in LIST_OPERATORS
            field_type = (
                OPERATORS_TYPES.get(operator_func)
                or field_filter.query_param_type
                or field_filter.field.type.python_type
            )
            name = f'{field_name}__{operator_name}'
            field_definitions.append(
                (
                    name,
                    List[field_type] if is_list else field_type,
                    Query(None, alias=f'{name}{[] if is_list else ""}')
                )
            )

    @property
    def filter_query(self):
        _filter_query = []
        for _field in self.__dataclass_fields__:
            if (value := getattr(self, _field, None)) is None:
                continue
            if isinstance(value, datetime):
                value = value.replace(tzinfo=None)
            _field_name, operator = _field.rsplit('__', 1)
            cast_type = available_fields[_field_name].cast_type
            _filter_query.append(
                available_fields[_field_name].operators[operator](
                    available_fields[_field_name].field,
                    cast_type(value)
                )
            )
        return _filter_query

    return make_dataclass('FilterQueryParams', field_definitions, namespace={
        'filter_query': filter_query
    })

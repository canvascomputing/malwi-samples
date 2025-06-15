from dataclasses import dataclass
from typing import (
    Any,
    List,
)
from unittest.mock import (
    MagicMock,
    patch,
)

import pytest

from fastapi_toolkit.dependencies import filter_by_fields
from fastapi_toolkit.filters import filter_
from fastapi_toolkit.filters.func import (
    contained_by,
    contains,
    eq,
    gt,
    in_,
    is_null,
    lte,
)
from tests.models import Book


@dataclass
class QueryMock:
    default: Any
    alias: str


@patch('fastapi_toolkit.dependencies.filter.Query', QueryMock)
class TestFilterResult:
    @pytest.mark.parametrize(
        ('test_fields', 'result_fields'),
        (
            (
                {
                    'title': filter_(Book.title, (eq,)),
                    'page_amount': filter_(Book.page_amount, (gt, lte), str),
                },
                {
                    'title__eq': QueryMock(None, alias='title__eq'),
                    'page_amount__gt': QueryMock(
                        None, alias='page_amount__gt'
                    ),
                    'page_amount__lte': QueryMock(
                        None, alias='page_amount__lte'
                    )
                }
            ),
            (
                {
                    'title': filter_(Book.title, (in_, contains)),
                    'page_amount': filter_(
                        Book.page_amount, (is_null, contained_by), str
                    ),
                },
                {
                    'title__in': QueryMock(None, alias='title__in[]'),
                    'title__contains': QueryMock(
                        None, alias='title__contains[]'
                    ),
                    'page_amount__is_null': QueryMock(
                        None, alias='page_amount__is_null'
                    ),
                    'page_amount__contained_by': QueryMock(
                        None, alias='page_amount__contained_by[]'
                    )
                }
            ),
        )
    )
    def test_dataclass__ok(
            self, test_fields: dict, result_fields: dict
    ):
        result = filter_by_fields(test_fields)
        assert result.__name__ == 'FilterQueryParams'
        for field_name in result.__dataclass_fields__:
            assert getattr(result, field_name) == result_fields[field_name]

    @pytest.mark.parametrize(
        ('test_fields', 'result_annotations'),
        (
            (
                {
                    'title': filter_(Book.title, (eq,)),
                    'page_amount': filter_(Book.page_amount, (gt, lte), str),
                },
                {
                    'title__eq': str,
                    'page_amount__gt': int,
                    'page_amount__lte': int,
                }
            ),
            (
                {
                    'title': filter_(Book.title, (in_, contains)),
                    'page_amount': filter_(
                        Book.page_amount, (is_null, contained_by), str
                    ),
                },
                {
                    'title__in': List[str],
                    'title__contains': List[str],
                    'page_amount__is_null': bool,
                    'page_amount__contained_by': List[int]
                },
            ),
            (
                {
                    'title': filter_(
                        Book.title, (eq, contains), query_param_type=int
                    ),
                    'page_amount': filter_(Book.title, (gt, ), int, str),
                },
                {
                    'title__eq': int,
                    'title__contains': List[int],
                    'page_amount__gt': str,
                }
            )
        )
    )
    def test_dataclass__annotations_ok(
            self, test_fields: dict, result_annotations: dict
    ):
        result = filter_by_fields(test_fields)
        assert result.__name__ == 'FilterQueryParams'
        for field_name, annotation in result.__annotations__.items():
            assert annotation is result_annotations[field_name]


@patch('fastapi_toolkit.dependencies.filter.Query', QueryMock)
class TestFilterQuery:
    @pytest.fixture
    def in_mock(self) -> MagicMock:
        return MagicMock()

    @pytest.fixture
    def eq_mock(self) -> MagicMock:
        return MagicMock()

    @pytest.fixture
    def title_mock(self, in_mock: MagicMock, eq_mock: MagicMock) -> MagicMock:
        return MagicMock(
            in_=in_mock, __eq__=eq_mock, type=MagicMock(python_type=str)
        )

    def test_filter_query__ok(
            self, in_mock: MagicMock, eq_mock: MagicMock, title_mock: MagicMock
    ):
        test_value = 'test_value'
        test_fields = {'title': filter_(title_mock, (in_, eq)), }
        queries = filter_by_fields(test_fields)(
            title__in=[test_value],
            title__eq=test_value,
        ).filter_query

        assert len(queries) == 2
        in_mock.assert_called_once_with([test_value])
        eq_mock.assert_called_once_with(test_value)

    def test_filter_query__cast_type_ok(
            self, eq_mock: MagicMock, title_mock: MagicMock
    ):
        test_value = '100'
        result_value = 101
        test_fields = {
            'title': filter_(title_mock, (eq, ), lambda x: int(x) + 1)
        }
        queries = filter_by_fields(test_fields)(
            title__eq=test_value,
        ).filter_query

        assert len(queries) == 1
        eq_mock.assert_called_once_with(result_value)

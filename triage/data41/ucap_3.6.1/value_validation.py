from __future__ import annotations

from types import MappingProxyType
from typing import Any, Sequence

import numpy as np
import numpy.typing as npt

from ucap.common.discrete_function import DiscreteFunction
from ucap.common.discrete_function_list import DiscreteFunctionList
from ucap.common.value_type import ValueType, _ArrayLikeTypeInternal

from .numeric_array_validation import (
    _make_immutable,
    _validate_and_normalize_numeric_array,
)

_numpy_type_to_value_type_aux_map: MappingProxyType[
    np.dtype, tuple[ValueType, ValueType, ValueType]
] = MappingProxyType(
    {
        ValueType.BOOLEAN.value.numpy_dtype: (
            ValueType.BOOLEAN,
            ValueType.BOOLEAN_ARRAY,
            ValueType.BOOLEAN_ARRAY_2D,
        ),
        ValueType.BYTE.value.numpy_dtype: (
            ValueType.BYTE,
            ValueType.BYTE_ARRAY,
            ValueType.BYTE_ARRAY_2D,
        ),
        ValueType.SHORT.value.numpy_dtype: (
            ValueType.SHORT,
            ValueType.SHORT_ARRAY,
            ValueType.SHORT_ARRAY_2D,
        ),
        ValueType.INT.value.numpy_dtype: (
            ValueType.INT,
            ValueType.INT_ARRAY,
            ValueType.INT_ARRAY_2D,
        ),
        ValueType.LONG.value.numpy_dtype: (
            ValueType.LONG,
            ValueType.LONG_ARRAY,
            ValueType.LONG_ARRAY_2D,
        ),
        ValueType.FLOAT.value.numpy_dtype: (
            ValueType.FLOAT,
            ValueType.FLOAT_ARRAY,
            ValueType.FLOAT_ARRAY_2D,
        ),
        ValueType.DOUBLE.value.numpy_dtype: (
            ValueType.DOUBLE,
            ValueType.DOUBLE_ARRAY,
            ValueType.DOUBLE_ARRAY_2D,
        ),
    }
)


def maybe_infer_value_type(value) -> ValueType | None:  # noqa: PLR0911, C901
    if isinstance(value, DiscreteFunction):
        return ValueType.DISCRETE_FUNCTION
    if isinstance(value, DiscreteFunctionList):
        return ValueType.DISCRETE_FUNCTION_LIST
    if isinstance(value, np.ndarray):
        if value.ndim > 2:  # noqa: PLR2004
            raise ValueError("Unexpected array shape: max 2D")
        if value.dtype in _numpy_type_to_value_type_aux_map:
            return _numpy_type_to_value_type_aux_map[value.dtype][value.ndim]
        if _is_numpy_string_array(value):
            return (
                ValueType.STRING,
                ValueType.STRING_ARRAY,
                ValueType.STRING_ARRAY_2D,
            )[value.ndim]

        return None
    if isinstance(value, (bool, np.bool_)):
        return ValueType.BOOLEAN
    if isinstance(value, np.number):
        return _numpy_type_to_value_type_aux_map[value.dtype][0]
    if isinstance(value, int):
        # For retro-compatibility
        return ValueType.INT
    if isinstance(value, float):
        # For retro-compatibility
        return ValueType.DOUBLE
    if isinstance(value, str):
        return ValueType.STRING
    return None


def _is_numpy_string_array(array: npt.NDArray):
    return array.dtype.kind == "U"


def _is_numpy_scalar_string(value):
    return (
        isinstance(value, np.ndarray)
        and _is_numpy_string_array(value)
        and value.shape == ()
    )


def _validate_1d_string_array(
    value,
) -> Sequence[str] | npt.NDArray[np.str_]:
    if isinstance(value, (tuple, list)):
        if any(not isinstance(s, str) for s in value):
            raise TypeError("The sequence contains non-string values")
        return tuple(value)

    if isinstance(value, np.ndarray):
        if not _is_numpy_string_array(value):
            raise TypeError(
                f"Expected string sequence, got {value.dtype} instead"
            )
        _make_immutable(value)
        return value

    raise TypeError(f"Expected 1D string sequence, got {type(value)}")


def _validate_2d_string_array(
    value,
) -> Sequence[Sequence[str] | npt.NDArray[np.str_]] | npt.NDArray[np.str_]:
    if isinstance(value, (list, tuple)):
        try:
            matrix = tuple(map(_validate_1d_string_array, value))
        except TypeError as exc:
            raise TypeError(
                "Expected 2D string sequence, but some rows are not valid"
            ) from exc

        if any(n_cols != len(matrix[0]) for n_cols in map(len, matrix)):
            raise ValueError(
                "Expected 2D string sequence, but rows have different sizes"
            )
        return matrix

    if isinstance(value, np.ndarray):
        if not _is_numpy_string_array(value):
            raise TypeError(
                f"Expected 2D string sequence, but got {value.dtype}"
            )
        if value.ndim != 2:  # noqa: PLR2004
            raise TypeError(
                f"Expected 2D string sequence, got {value.ndim}D instead"
            )
        _make_immutable(value)
        return value

    raise TypeError(f"Expected 2D string sequence, got {type(value)}")


def validate_and_normalize(value, value_type: ValueType) -> Any:
    if isinstance(value_type.value, _ArrayLikeTypeInternal):
        return _validate_and_normalize_numeric_array(
            value,
            value_type.value.numpy_dtype,
            value_type.value.number_of_dimensions,
        )

    if value_type == ValueType.STRING:
        if isinstance(value, str) or _is_numpy_scalar_string(value):
            return value
        raise TypeError(f"Expected string, got {type(value)}")

    if value_type == ValueType.STRING_ARRAY:
        return _validate_1d_string_array(value)

    if value_type == ValueType.STRING_ARRAY_2D:
        return _validate_2d_string_array(value)

    if value_type == ValueType.DISCRETE_FUNCTION:
        if isinstance(value, DiscreteFunction):
            return value
        raise TypeError(f"Expected DiscreteFunction, got {type(value)}")

    if value_type == ValueType.DISCRETE_FUNCTION_LIST:
        if isinstance(value, DiscreteFunctionList):
            return value
        raise TypeError(f"Expected DiscreteFunctionList, got {type(value)}")

    raise TypeError(f"Unknown ValueType {value_type}")

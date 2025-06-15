from __future__ import annotations

import sys
from dataclasses import dataclass
from enum import Enum
from types import MappingProxyType

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override

import numpy as np

from .discrete_function import DiscreteFunction  # noqa: F401
from .discrete_function_list import DiscreteFunctionList  # noqa: F401


@dataclass(frozen=True, repr=False)
class _ValueTypeInternal:
    # Internal
    japc_value_type: str
    # Internal
    number_of_dimensions: int

    # Overridden because we should not show the class name
    def __repr__(self):
        return f"(japc_value_type='{self.japc_value_type}', number_of_dimensions={self.number_of_dimensions})"


@dataclass(frozen=True, repr=False)
class _ArrayLikeTypeInternal(_ValueTypeInternal):
    # Internal
    numpy_dtype: np.dtype

    # Overridden because we should not show the class name
    @override
    def __repr__(self):
        return f"(japc_value_type='{self.japc_value_type}', numpy_dtype={self.numpy_dtype}, number_of_dimensions={self.number_of_dimensions})"


class ValueType(Enum):
    """Enumeration for supported value types"""

    BOOLEAN = _ArrayLikeTypeInternal(
        japc_value_type="boolean",
        numpy_dtype=np.dtype(bool),
        number_of_dimensions=0,
    )
    BOOLEAN_ARRAY = _ArrayLikeTypeInternal(
        japc_value_type="boolean[]",
        numpy_dtype=BOOLEAN.numpy_dtype,
        number_of_dimensions=1,
    )
    BOOLEAN_ARRAY_2D = _ArrayLikeTypeInternal(
        japc_value_type="boolean[][]",
        numpy_dtype=BOOLEAN.numpy_dtype,
        number_of_dimensions=2,
    )

    BYTE = _ArrayLikeTypeInternal(
        japc_value_type="byte",
        numpy_dtype=np.dtype(np.int8),
        number_of_dimensions=0,
    )
    BYTE_ARRAY = _ArrayLikeTypeInternal(
        japc_value_type="byte[]",
        numpy_dtype=BYTE.numpy_dtype,
        number_of_dimensions=1,
    )
    BYTE_ARRAY_2D = _ArrayLikeTypeInternal(
        japc_value_type="byte[][]",
        numpy_dtype=BYTE.numpy_dtype,
        number_of_dimensions=2,
    )

    SHORT = _ArrayLikeTypeInternal(
        japc_value_type="short",
        numpy_dtype=np.dtype(np.int16),
        number_of_dimensions=0,
    )
    SHORT_ARRAY = _ArrayLikeTypeInternal(
        japc_value_type="short[]",
        numpy_dtype=SHORT.numpy_dtype,
        number_of_dimensions=1,
    )
    SHORT_ARRAY_2D = _ArrayLikeTypeInternal(
        japc_value_type="short[][]",
        numpy_dtype=SHORT.numpy_dtype,
        number_of_dimensions=2,
    )

    INT = _ArrayLikeTypeInternal(
        japc_value_type="int",
        numpy_dtype=np.dtype(np.int32),
        number_of_dimensions=0,
    )
    INT_ARRAY = _ArrayLikeTypeInternal(
        japc_value_type="int[]",
        numpy_dtype=INT.numpy_dtype,
        number_of_dimensions=1,
    )
    INT_ARRAY_2D = _ArrayLikeTypeInternal(
        japc_value_type="int[][]",
        numpy_dtype=INT.numpy_dtype,
        number_of_dimensions=2,
    )

    LONG = _ArrayLikeTypeInternal(
        japc_value_type="long",
        numpy_dtype=np.dtype(int),
        number_of_dimensions=0,
    )
    LONG_ARRAY = _ArrayLikeTypeInternal(
        japc_value_type="long[]",
        numpy_dtype=LONG.numpy_dtype,
        number_of_dimensions=1,
    )
    LONG_ARRAY_2D = _ArrayLikeTypeInternal(
        japc_value_type="long[][]",
        numpy_dtype=LONG.numpy_dtype,
        number_of_dimensions=2,
    )

    FLOAT = _ArrayLikeTypeInternal(
        japc_value_type="float",
        numpy_dtype=np.dtype(np.float32),
        number_of_dimensions=0,
    )
    FLOAT_ARRAY = _ArrayLikeTypeInternal(
        japc_value_type="float[]",
        numpy_dtype=FLOAT.numpy_dtype,
        number_of_dimensions=1,
    )
    FLOAT_ARRAY_2D = _ArrayLikeTypeInternal(
        japc_value_type="float[][]",
        numpy_dtype=FLOAT.numpy_dtype,
        number_of_dimensions=2,
    )

    DOUBLE = _ArrayLikeTypeInternal(
        japc_value_type="double",
        numpy_dtype=np.dtype(np.float64),
        number_of_dimensions=0,
    )
    DOUBLE_ARRAY = _ArrayLikeTypeInternal(
        japc_value_type="double[]",
        numpy_dtype=DOUBLE.numpy_dtype,
        number_of_dimensions=1,
    )
    DOUBLE_ARRAY_2D = _ArrayLikeTypeInternal(
        japc_value_type="double[][]",
        numpy_dtype=DOUBLE.numpy_dtype,
        number_of_dimensions=2,
    )

    STRING = _ValueTypeInternal(
        japc_value_type="String", number_of_dimensions=0
    )
    STRING_ARRAY = _ValueTypeInternal(
        japc_value_type="String[]", number_of_dimensions=1
    )
    STRING_ARRAY_2D = _ValueTypeInternal(
        japc_value_type="String[][]", number_of_dimensions=2
    )

    DISCRETE_FUNCTION = _ValueTypeInternal(
        japc_value_type="DiscreteFunction", number_of_dimensions=0
    )
    DISCRETE_FUNCTION_LIST = _ValueTypeInternal(
        japc_value_type="DiscreteFunctionList", number_of_dimensions=1
    )


def _maybe_get_value_type(name: str) -> ValueType | None:
    if hasattr(ValueType, name):
        return getattr(ValueType, name)
    return None


_japc_type_to_value_type_aux_map: MappingProxyType[str, ValueType] = (
    MappingProxyType(
        {
            value_type.value.japc_value_type: value_type
            for value_type in ValueType
        }
    )
)


def _maybe_get_japc_type(name: str) -> ValueType | None:
    return _japc_type_to_value_type_aux_map.get(name, None)


def maybe_value_type_from_str(string_value: str) -> ValueType | None:
    if output := _maybe_get_value_type(string_value.upper()):
        return output
    if output := _maybe_get_japc_type(string_value):
        return output
    return None

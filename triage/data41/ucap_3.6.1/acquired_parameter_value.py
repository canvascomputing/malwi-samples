from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Literal, overload

if TYPE_CHECKING:
    import numpy as np
    import numpy.typing as npt

    from ucap.common.discrete_function import DiscreteFunction
    from ucap.common.discrete_function_list import DiscreteFunctionList

from .internal.value_validation import (
    maybe_infer_value_type,
    validate_and_normalize,
)
from .value_header import ValueHeader
from .value_type import ValueType, maybe_value_type_from_str


@dataclass(frozen=True)
class ValueEntry:
    value: Any
    type: ValueType
    _normalized_value: Any = None

    @property
    def normalized_value(self):
        if self._normalized_value is None:
            return validate_and_normalize(
                value=self.value, value_type=self.type
            )
        return self._normalized_value


class AcquiredParameterValue:
    """
    # noqa: D404
    This class represents the value of a parameter that has been acquired from the device
    (typically a measurement).
    """

    def __init__(self, parameter_name: str, header: ValueHeader | None = None):
        """
        Creates a new and empty instance of AcquiredParameterValue with provided parameter name.

        Empty instance means that the dict of values associated with it(#values property) will be empty.

        Parameters
        ----------
        parameter_name: str
            the name of the parameter of which this instance of AcquiredParametervalue should be the representation of
        header: ValueHeader, optional
            the value header representing the time of acquiring the data. When None provided it will be filled
            with an empty ValueHeader, by default None

        Returns
        -------
        AcquiredParameterValue
            new instance of AcquiredParameterValue

        """
        self._parameter_name = parameter_name
        if header is None:
            header = ValueHeader()
        self._header: ValueHeader = header
        self._values: dict[str, ValueEntry] = {}

    @property
    def parameter_name(self) -> str:
        """
        Returns the parameter name the value has been read from

        Returns
        -------
        str
            the parameter name the value has been read from

        """
        return self._parameter_name

    @property
    def header(self) -> ValueHeader:
        """
        Returns the ValueHeader associated with this value.

        Returns
        -------
        ValueHeader
            the header associated with this value.

        """
        return self._header

    @property
    def field_names(self) -> tuple[str, ...]:
        """
        Returns field names acquired from the parameter.

        Returns
        -------
        tuple[str, ...]
            tuple containing field names

        """
        return tuple(self._values.keys())

    @property
    def values(self) -> dict[str, tuple[Any, ValueType]]:
        """
        Returns values of all fields acquired from the parameter in form of a dictionary,
        where the key is the field name and the value is a tuple containing the value itself
        and a string representing the value type.

        If the value was acquired from the field directly, the dictionary will contain
        one key:value pair only where the key be equal to 'value' string.

        Returns
        -------
        dict[str, tuple[VT, ValueType]]
            dictionary containing values for all fields associated with the parameter the value was acquired from

        """
        return {
            name: self.get_value_and_type(name) for name in self.field_names
        }

    def get_value_and_type(
        self, field_name: str = "value"
    ) -> tuple[Any, ValueType]:
        """
        Returns the value of a single field acquired from the parameter in form
        of a tuple, where the first element is the value itself, while the second one
        is a string representing the value type (tuple[Any, str])

        Parameters
        ----------
        field_name : str, optional
            The name of the field of the property of which the value should be retrieved.
            If not specified it is assumed that the subscription was defined directly to the field itself,
            by default "value"

        Returns
        -------
        tuple[Any, ValueType]
            tuple containing the actual value as the first element, and it's ValueType

        """
        return self.get_value(field_name), self.get_type(field_name)

    def get_value(self, field_name: str = "value") -> Any:
        """
        Returns the value of a single field acquired from the parameter.

        Parameters
        ----------
        field_name : str, optional
            The name of the field of the property of which the value should be retrieved.
            If not specified it is assumed that the subscription was defined directly to the field itself,
            by default 'value'

        Returns
        -------
        Any
            the actual value of the field

        """
        return self._values[field_name].value

    @overload
    def get_value_with_type(
        self, *, field_name: str, value_type: Literal[ValueType.BOOLEAN]
    ) -> bool: ...

    @overload
    def get_value_with_type(
        self,
        *,
        field_name: str,
        value_type: Literal[
            ValueType.BOOLEAN_ARRAY, ValueType.BOOLEAN_ARRAY_2D
        ],
    ) -> npt.NDArray[np.bool_]: ...

    @overload
    def get_value_with_type(
        self,
        *,
        field_name: str,
        value_type: Literal[
            ValueType.BYTE, ValueType.SHORT, ValueType.INT, ValueType.LONG
        ],
    ) -> int: ...

    @overload
    def get_value_with_type(
        self,
        *,
        field_name: str,
        value_type: Literal[ValueType.BYTE_ARRAY, ValueType.BYTE_ARRAY_2D],
    ) -> npt.NDArray[np.int8]: ...

    @overload
    def get_value_with_type(
        self,
        *,
        field_name: str,
        value_type: Literal[
            ValueType.SHORT_ARRAY,
            ValueType.SHORT_ARRAY_2D,
        ],
    ) -> npt.NDArray[np.int16]: ...

    @overload
    def get_value_with_type(
        self,
        *,
        field_name: str,
        value_type: Literal[ValueType.INT_ARRAY, ValueType.INT_ARRAY_2D],
    ) -> npt.NDArray[np.int32]: ...

    @overload
    def get_value_with_type(
        self,
        *,
        field_name: str,
        value_type: Literal[
            ValueType.LONG_ARRAY,
            ValueType.LONG_ARRAY_2D,
        ],
    ) -> npt.NDArray[np.int64]: ...

    @overload
    def get_value_with_type(
        self,
        *,
        field_name: str,
        value_type: Literal[ValueType.FLOAT, ValueType.DOUBLE],
    ) -> float: ...

    @overload
    def get_value_with_type(
        self,
        *,
        field_name: str,
        value_type: Literal[ValueType.FLOAT_ARRAY, ValueType.FLOAT_ARRAY_2D],
    ) -> npt.NDArray[np.float32]: ...

    @overload
    def get_value_with_type(
        self,
        *,
        field_name: str,
        value_type: Literal[
            ValueType.DOUBLE_ARRAY,
            ValueType.DOUBLE_ARRAY_2D,
        ],
    ) -> npt.NDArray[np.float64]: ...

    @overload
    def get_value_with_type(
        self, *, field_name: str, value_type: Literal[ValueType.STRING,]
    ) -> str: ...

    @overload
    def get_value_with_type(
        self,
        *,
        field_name: str,
        value_type: Literal[ValueType.STRING_ARRAY,],
    ) -> tuple[str, ...]: ...

    @overload
    def get_value_with_type(
        self,
        *,
        field_name: str,
        value_type: Literal[ValueType.STRING_ARRAY_2D,],
    ) -> tuple[tuple[str, ...], ...]: ...

    @overload
    def get_value_with_type(
        self,
        *,
        field_name: str,
        value_type: Literal[ValueType.DISCRETE_FUNCTION],
    ) -> DiscreteFunction: ...

    @overload
    def get_value_with_type(
        self,
        *,
        field_name: str,
        value_type: Literal[ValueType.DISCRETE_FUNCTION_LIST],
    ) -> DiscreteFunctionList: ...

    # TODO Track progress on https://github.com/numpy/numpy/issues/16544
    def get_value_with_type(
        self, *, field_name: str = "value", value_type: ValueType
    ) -> Any:
        """
        Returns the value of a single field acquired from the parameter.

        Parameters
        ----------
        field_name : str, optional
            The name of the field of the property of which the value should be retrieved.
            If not specified it is assumed that the subscription was defined directly to the field itself,
            by default 'value'
        value_type: ValueType
            Expected value type for the field. Throws if the type does not match.

        Returns
        -------
        Any
            the actual value of the field

        """
        if value_type is None or not isinstance(value_type, ValueType):
            raise ValueError(
                f"Unexpected argument for value_type: {value_type}"
            )

        value, actual_type = self.get_value_and_type(field_name)
        if actual_type == value_type:
            return value
        raise TypeError(f"Expected {value_type}, got {actual_type}")

    def get_type(self, field_name: str = "value") -> ValueType:
        """
        Returns the type of the value of a single field acquired from the parameter.

        Parameters
        ----------
        field_name : str, optional
            The name of the field of the property of which the value type should be retrieved.
            If not specified it is assumed that the subscription was defined directly to the field itself,
            by default 'value'

        Returns
        -------
        ValueType
            represents the type of the value

        """
        return self._values[field_name].type

    def update_value(
        self,
        field_name: str = "value",
        # These are kept `None` just for retro-compatibility
        value: Any = None,
        value_type: str | ValueType | None = None,
    ):
        """
        Adds (or updates if it was already existing) a new value for a given field.

        Parameters
        ----------
        field_name : str, optional
            the name of the field the value is associated with, by default 'value'
        value : VT, optional
            the value itself, by default None
        value_type : ValueType, optional
            representing the value type. When None, and the value type is one of simple types
            it will be automatically filled to that simple type, by default None

        """
        if not isinstance(field_name, str):
            raise TypeError(f"Field name is not a string: {field_name}")

        if value_type is None:
            value_type = self._infer_value_type_or_throw(field_name, value)
        elif isinstance(value_type, str) and not (
            value_type := maybe_value_type_from_str(value_type)
        ):
            raise KeyError(f"Unknown ValueType {value_type}")

        if not isinstance(value_type, ValueType):
            raise TypeError(f"Invalid ValueType provided: {type(value_type)}")
        if (
            field_name in self._values
            and value_type != self._values[field_name].type
        ):
            raise TypeError(
                f"Unsupported update: old ValueType is {self._values[field_name].type}, new is {value_type}"
            )

        normalized_value = validate_and_normalize(
            value=value, value_type=value_type
        )
        self._values[field_name] = ValueEntry(
            value=value, _normalized_value=normalized_value, type=value_type
        )

    def _infer_value_type_or_throw(
        self, field_name: str, value: Any
    ) -> ValueType:
        if field_name in self._values:
            return self._values[field_name].type

        value_type = maybe_infer_value_type(value)
        if not value_type:
            raise TypeError(
                f"ValueType for {type(value)} could not be inferred"
            )
        return value_type

    def __repr__(self):
        return (
            f"AcquiredParameterValue(\n"
            f"\tparameter_name={self._parameter_name}\n"
            f"\theader={self._header}\n"
            f"\tvalues={self._values}\n"
            f")"
        )

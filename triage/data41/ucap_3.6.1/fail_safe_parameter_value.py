from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .acquired_parameter_value import AcquiredParameterValue
from .parameter_exception import ParameterException

if TYPE_CHECKING:
    from .value_header import ValueHeader


@dataclass(frozen=True)
class FailSafeParameterValue:
    """
    Represents an AcquiredParameterValue or ParameterException.
    Two cases are possible:

    * The received/to be published value is a valid AcquiredParameterValue, the `value` property
      is present and `exception` is `None`
    * The received/to be published value is a ParameterException, the `exception` property
      is present and `value` is `None`

    The `parameter_name` and `header` properties shall be always present.

    Attributes
        value_or_exception : Union[AcquiredParameterValue, ParameterException]
                Value or exception contained in this parameter value.

    """

    value_or_exception: AcquiredParameterValue | ParameterException

    @property
    def parameter_name(self) -> str:
        """
        Returns the parameter name.

        Returns
        -------
        str
            the parameter name

        """
        return self.value_or_exception.parameter_name

    @property
    def header(self) -> ValueHeader:
        """
        Returns the parameter header.

        Returns
        -------
        ValueHeader
            the parameter header

        """
        return self.value_or_exception.header

    @property
    def value(self) -> AcquiredParameterValue | None:
        """
        Returns the AcquiredParameterValue obtained from the parameter.

        Returns
        -------
        Optional[AcquiredParameterValue]
            object with all values acquired from the parameter

        """
        return (
            self.value_or_exception
            if isinstance(self.value_or_exception, AcquiredParameterValue)
            else None
        )

    @property
    def exception(self) -> ParameterException | None:
        """
        Returns the ParameterException object representing the information about
        why the data was not correctly acquired.

        Returns
        -------
        Optional[ParameterException]
            the exception that occured during value acquisition

        """
        return (
            self.value_or_exception
            if isinstance(self.value_or_exception, ParameterException)
            else None
        )

from dataclasses import dataclass, field

from .value_header import ValueHeader


@dataclass(frozen=True)
class ParameterException:
    """
    Represents a parameter exception to be published.

    Attributes
        message : str
                message shortly summarizing the exception cause
        parameter_name : str, optional
            the name of the parameter
        header: ValueHeader, optional
            the value header representing the time of acquiring the data. When None provided it will be filled
            with an empty ValueHeader, by default None

    """

    message: str = ""
    parameter_name: str = ""
    header: ValueHeader = field(default_factory=ValueHeader)

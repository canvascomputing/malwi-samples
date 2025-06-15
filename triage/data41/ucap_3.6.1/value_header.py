from dataclasses import dataclass

from .selectors import Selector, Selectors
from .update_type import UpdateType

_NANOS_IN_MILLIS = 1e6


@dataclass(frozen=True)
class ValueHeader:
    """
    Represents a header providing information on a value.

    Attributes
        acq_stamp : int
            the acquisition timestamp nanos, by default 0
        cycle_stamp : int
            the cycle timestamp nanos, by default 0
        selector : Selector
            tye cycle selector, by default `Selectors.NO_SELECTOR`
        update_type : UpdateType
            the type of the update, by default `UpdateType.NORMAL`

    """

    acq_stamp: int = 0
    cycle_stamp: int = 0
    selector: Selector = Selectors.NO_SELECTOR
    update_type: UpdateType = UpdateType.NORMAL

    def __post_init__(self):
        if self.selector is None:
            raise ValueError(
                f"Invalid selector: {self.selector} (did you mean Selectors.NO_SELECTOR?)"
            )
        if not isinstance(self.update_type, UpdateType):
            raise TypeError(
                f"Update type must be enum from UpdateType: {type(self.update_type)}"
            )

    @property
    def acq_stamp_millis(self) -> float:
        """
        Returns the acquisition Time Stamp (UTC in milliseconds). It is the absolute time in milliseconds this value has
        been acquired. If the timestamp is not known or not relevant the constant 0 should be returned.

        Returns
        -------
        float
            the absolute time in milliseconds this value has been acquired.

        """
        return self.acq_stamp / _NANOS_IN_MILLIS

    @property
    def cycle_stamp_millis(self) -> float:
        """
        Returns unique time stamp that identifies a unique cycle occurrence. Time UTC (in milliseconds).
        If the cycleStamp is not known or not relevant 0 should be returned.

        Returns
        -------
        float
            the unique time stamp that identifies a unique cycle occurrence this value belongs to in milliseconds

        """
        return self.cycle_stamp / _NANOS_IN_MILLIS

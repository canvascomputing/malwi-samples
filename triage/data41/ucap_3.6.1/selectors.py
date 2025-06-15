from __future__ import annotations

from dataclasses import dataclass
from typing import Any


# TODO DEV NOTE representation is not trivial as MPV object is missing from the Python part (as it is part of APV)
@dataclass(frozen=True, repr=False)
class Selector:
    """
    Represents a cycle selector.

    Attributes
        selector_id : str
            selector id (i.e., cycle name)
        data_filter : Any
            data filter (only for information)

    """

    selector_id: str
    # NOTE data_filter is only for information (UCAP v2-rc)
    data_filter: Any | None = None

    def __post_init__(self):
        if self.selector_id is None:
            raise ValueError(f"Invalid selector id: {self.selector_id}")

    def __repr__(self):
        if self.data_filter:
            return f"Selector(selector_id={self.selector_id}, data_filter={self.data_filter})"
        return f"Selector(selector_id={self.selector_id})"


class Selectors:
    """Non-PPM, non-cycle-bound selector."""

    NO_SELECTOR = Selector("")

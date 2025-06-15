from enum import Enum


class UpdateType(Enum):
    """Represents possible types of updates in ValueHeader instances."""

    NORMAL = "NORMAL"
    FIRST_UPDATE = "FIRST_UPDATE"
    IMMEDIATE_UPDATE = "IMMEDIATE_UPDATE"

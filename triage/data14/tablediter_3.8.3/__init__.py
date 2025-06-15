from __future__ import annotations

from .tablediter import (
    ALL,
    DEFAULT,
    DOUBLE_BORDER,
    FRAME,
    HEADER,
    MARKDOWN,
    MSWORD_FRIENDLY,
    NONE,
    ORGMODE,
    PLAIN_COLUMNS,
    RANDOM,
    SINGLE_BORDER,
    tablediter,
    TableHandler,
    from_csv,
    from_db_cursor,
    from_html,
    from_html_one,
    from_json,
)

__all__ = [
    "ALL",
    "DEFAULT",
    "DOUBLE_BORDER",
    "SINGLE_BORDER",
    "FRAME",
    "HEADER",
    "MARKDOWN",
    "MSWORD_FRIENDLY",
    "NONE",
    "ORGMODE",
    "PLAIN_COLUMNS",
    "RANDOM",
    "tablediter",
    "TableHandler",
    "from_csv",
    "from_db_cursor",
    "from_html",
    "from_html_one",
    "from_json",
]

import importlib.metadata

__version__ = importlib.metadata.version(__name__)

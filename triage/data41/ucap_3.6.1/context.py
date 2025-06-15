"""
Transformation context.

Values of the variables defined in this module will be injected during runtime by ucap-python-server when starting
given transformation. Default values are provided to enable testing.
"""

from __future__ import annotations

from typing import Any

device_name: str = "TEST_DEVICE"
transformation_name: str = "TEST_TRANSFORMATION"
published_property_name: str = "TestProperty"
published_property_names: list[str] = ["TestProperty", "TestProperty2"]
published_parameter_name: str = "TEST_DEVICE/TestProperty"
published_parameter_names: list[str] = [
    "TEST_DEVICE/TestProperty",
    "TEST_DEVICE/TestProperty2",
]
configuration: dict[str, Any] = {}

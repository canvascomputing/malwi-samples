from unittest.mock import patch

import pytest

from ucap.common.acquired_parameter_value import AcquiredParameterValue
from ucap.common.event import Event
from ucap.common.fail_safe_parameter_value import FailSafeParameterValue
from ucap.common.parameter_exception import ParameterException
from ucap.common.selectors import Selector
from ucap.common.value_type import ValueType


def test_creation_time():
    event = Event()
    event._creation_time = 20
    assert event.creation_time == 20
    assert event.event_creation_time == 20


def test_timeout_reached():
    event = Event()
    event._timeout_reached = True
    assert event.timeout_reached is True


def test_value_names():
    event = Event()
    event._value_names = ("value1", "value2")
    assert event.value_names == ("value1", "value2")


def test_missing_value_names():
    event = Event()
    event._missing_value_names = ("value1", "value2")
    assert event.missing_value_names == ("value1", "value2")


def test_trigger_name():
    event = Event()
    event._trigger_name = "value1"
    assert event.trigger_name == "value1"


def test_error_value_names():
    apv = AcquiredParameterValue(parameter_name="Acquisition")
    apv.update_value("field1", 20, ValueType.INT)
    apv.update_value("field2", 20.2, ValueType.DOUBLE)

    event = Event()
    event._value_names = ("value1", "value2", "value3")
    event._all_buffered_values = {
        "value1": (
            FailSafeParameterValue(apv),
            FailSafeParameterValue(ParameterException()),
        ),
        "value2": (FailSafeParameterValue(apv),),
        "value3": (FailSafeParameterValue(ParameterException()),),
    }
    assert event.error_value_names == ("value1", "value3")


def test_get_value():
    event = Event()
    event._all_buffered_values = {"value1": (10, 20)}
    assert event.get_value("value1") == 20


def test_get_value_missing():
    event = Event()
    event._all_buffered_values = {}
    assert event.get_value("value1") is None


def test_get_value_empty():
    event = Event()
    event._all_buffered_values = {"value1": ()}
    assert event.get_value("value1") is None


def test_convert_alias_to_selector_alias():
    assert (
        Event._convert_alias_to_selector_alias("value1", "ciao")
        == "value1@ciao"
    )


def test_convert_alias_to_selector_alias_with_selector():
    assert (
        Event._convert_alias_to_selector_alias("value1", Selector("sid"))
        == "value1@sid"
    )


def test_convert_alias_to_selector_alias_with_none_value_name():
    with pytest.raises(ValueError, match="Invalid value_name: None"):
        Event._convert_alias_to_selector_alias(None, Selector("sid"))


def test_convert_alias_to_selector_alias_with_none_selector():
    with pytest.raises(ValueError, match="Invalid selector: None"):
        Event._convert_alias_to_selector_alias("value1", None)


@pytest.mark.parametrize(
    "selector", ["some-selector", Selector("some-selector")]
)
def test_get_value_by_selector(selector):
    event = Event()
    event._all_buffered_values = {"value1@some-selector": (10, 20)}
    assert event.get_value_by_selector("value1", selector) == 20


def test_get_values():
    event = Event()
    event._all_buffered_values = {"value1": (10, 20)}
    assert event.get_values("value1") == (10, 20)


def test_get_values_missing():
    event = Event()
    event._all_buffered_values = ()
    assert event.get_values("value1") == ()


def test_get_values_empty():
    event = Event()
    event._all_buffered_values = {"value1": ()}
    assert event.get_values("value1") == ()


@pytest.mark.parametrize(
    "selector", ["some-selector", Selector("some-selector")]
)
def test_get_values_by_selector(selector):
    event = Event()
    event._all_buffered_values = {"value1@some-selector": (10, 20)}
    assert event.get_values_by_selector("value1", selector) == (10, 20)


def test_get_plain_value_and_type():
    apv = AcquiredParameterValue(parameter_name="Acquisition")
    apv.update_value("field1", 20, ValueType.INT)
    event = Event()
    event._all_buffered_values = {"value1": (FailSafeParameterValue(apv),)}
    assert event.get_plain_value_and_type("value1", "field1") == (
        20,
        ValueType.INT,
    )


def test_get_plain_value_and_type_with_exception():
    event = Event()
    event._all_buffered_values = {
        "value1": (FailSafeParameterValue(ParameterException()),)
    }
    assert event.get_plain_value_and_type("value1", "field1") == (None, None)


def test_get_plain_value_and_type_not_found():
    event = Event()
    event._all_buffered_values = {}
    assert event.get_plain_value_and_type("value1", "field1") == (None, None)


def test_get_plain_value_and_type_field_not_found():
    apv = AcquiredParameterValue(parameter_name="Acquisition")
    apv.update_value("field1", 20, ValueType.INT)
    event = Event()
    event._all_buffered_values = {"value1": (FailSafeParameterValue(apv),)}
    with pytest.raises(KeyError):
        event.get_plain_value_and_type("value1", "field2")


@pytest.mark.parametrize(
    "selector", ["some-selector", Selector("some-selector")]
)
def test_get_plain_value_and_type_by_selector(selector):
    event = Event()
    with patch.object(event, "get_plain_value_and_type") as gpvt:
        event.get_plain_value_and_type_by_selector("value1", selector, "field1")
    gpvt.assert_called_once_with("value1@some-selector", "field1")


def test_get_plain_value():
    apv = AcquiredParameterValue(parameter_name="Acquisition")
    apv.update_value("field1", 20, ValueType.INT)
    event = Event()
    event._all_buffered_values = {"value1": (FailSafeParameterValue(apv),)}
    with patch.object(event, "get_plain_value_and_type") as gpvt:
        event.get_plain_value("value1", "field1")
    gpvt.assert_called_once_with("value1", "field1")


@pytest.mark.parametrize(
    "selector", ["some-selector", Selector("some-selector")]
)
def test_get_plain_value_by_selector(selector):
    event = Event()
    with patch.object(event, "get_plain_value_and_type") as gpvt:
        event.get_plain_value_by_selector("value1", selector, "field1")
    gpvt.assert_called_once_with("value1@some-selector", "field1")


def test_get_plain_values_and_types():
    apv = AcquiredParameterValue(parameter_name="Acquisition")
    apv.update_value("field1", 20, ValueType.INT)
    apv.update_value("field2", 20.2, ValueType.DOUBLE)

    apv2 = AcquiredParameterValue(parameter_name="Acquisition")
    apv2.update_value("field1", "ciao", ValueType.STRING)
    apv2.update_value("field2", [True, False, True], ValueType.BOOLEAN_ARRAY)

    event = Event()
    event._all_buffered_values = {
        "value1": (FailSafeParameterValue(apv), FailSafeParameterValue(apv2))
    }
    output = event.get_plain_values_and_types("value1", "field2")
    assert output[0] == (20.2, ValueType.DOUBLE)
    assert tuple(output[1][0]) == (True, False, True)
    assert output[1][1] == ValueType.BOOLEAN_ARRAY


def test_get_plain_values_and_types_with_exception():
    apv = AcquiredParameterValue(parameter_name="Acquisition")
    apv.update_value("field1", 20, ValueType.INT)
    apv.update_value("field2", 20.2, ValueType.DOUBLE)

    event = Event()
    event._all_buffered_values = {
        "value1": (
            FailSafeParameterValue(apv),
            FailSafeParameterValue(ParameterException()),
        )
    }
    output = event.get_plain_values_and_types("value1", "field2")
    assert output[0] == (20.2, ValueType.DOUBLE)
    assert output[1] == (None, None)


def test_get_plain_values():
    apv = AcquiredParameterValue(parameter_name="Acquisition")
    apv.update_value("field1", 20, ValueType.INT)
    apv.update_value("field2", 20.2, ValueType.DOUBLE)

    apv2 = AcquiredParameterValue(parameter_name="Acquisition")
    apv2.update_value("field1", "ciao", ValueType.STRING)
    apv2.update_value("field2", [True, False, True], ValueType.BOOLEAN_ARRAY)

    event = Event()
    event._all_buffered_values = {
        "value1": (FailSafeParameterValue(apv), FailSafeParameterValue(apv2))
    }
    output = event.get_plain_values("value1", "field2")
    assert output[0] == 20.2
    assert tuple(output[1]) == (True, False, True)


def test_get_plain_values_with_exception():
    apv = AcquiredParameterValue(parameter_name="Acquisition")
    apv.update_value("field1", 20, ValueType.INT)
    apv.update_value("field2", 20.2, ValueType.DOUBLE)

    event = Event()
    event._all_buffered_values = {
        "value1": (
            FailSafeParameterValue(apv),
            FailSafeParameterValue(ParameterException()),
        )
    }
    output = event.get_plain_values("value1", "field2")
    assert output[0] == 20.2
    assert output[1] is None


@pytest.mark.parametrize(
    "selector", ["some-selector", Selector("some-selector")]
)
def test_get_plain_values_and_types_by_selector(selector):
    event = Event()
    with patch.object(event, "get_plain_values_and_types") as gpvt:
        event.get_plain_values_and_types_by_selector(
            "value1", selector, "field1"
        )
    gpvt.assert_called_once_with("value1@some-selector", "field1")


@pytest.mark.parametrize(
    "selector", ["some-selector", Selector("some-selector")]
)
def test_get_plain_values_by_selector(selector):
    event = Event()
    with patch.object(event, "get_plain_values") as gpvt:
        event.get_plain_values_by_selector("value1", selector, "field1")
    gpvt.assert_called_once_with("value1@some-selector", "field1")

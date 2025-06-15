import pytest

from ucap.common import Selector, Selectors, UpdateType, ValueHeader


def test_constructor_should_create_empty_object():
    value_header = ValueHeader()

    assert value_header.selector == Selectors.NO_SELECTOR
    assert value_header.acq_stamp == 0
    assert value_header.cycle_stamp == 0
    assert value_header.update_type == UpdateType.NORMAL


def test_constructor_should_create_with_provided_values():
    wanted_acq_stamp: int = 1234
    wanted_cycle_stamp: int = 5678
    wanted_selectore: Selector = Selector("agnes")
    wanted_update_type: UpdateType = UpdateType.NORMAL

    value_header = ValueHeader(
        acq_stamp=wanted_acq_stamp,
        cycle_stamp=wanted_cycle_stamp,
        selector=wanted_selectore,
        update_type=wanted_update_type,
    )

    assert wanted_acq_stamp == value_header.acq_stamp
    assert wanted_cycle_stamp == value_header.cycle_stamp
    assert wanted_selectore.selector_id == value_header.selector.selector_id
    assert wanted_update_type == value_header.update_type


def test_constructor_should_throw_exception_wrong_update_type():
    wanted_acq_stamp: int = 1234
    wanted_cycle_stamp: int = 5678
    wanted_selectore: Selector = Selector("agnes")
    wanted_update_type: str = "String-instead-of-UpdateType"

    with pytest.raises(
        TypeError, match="Update type must be enum from UpdateType.*"
    ):
        ValueHeader(
            acq_stamp=wanted_acq_stamp,
            cycle_stamp=wanted_cycle_stamp,
            selector=wanted_selectore,
            update_type=wanted_update_type,
        )


def test_acq_stamp_millis():
    value_header = ValueHeader(
        acq_stamp=int(5.0e6 + 0.5 * 1.0e6),
    )
    assert value_header.acq_stamp_millis == 5.5


def test_cycle_stamp_millis():
    value_header = ValueHeader(
        cycle_stamp=int(5.0e6 + 0.5 * 1.0e6),
    )
    assert value_header.cycle_stamp_millis == 5.5

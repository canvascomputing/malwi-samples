from ucap.common import ParameterException, Selectors, UpdateType, ValueHeader


def test_constructor_should_return_parameter_exception_with_provided_message():
    assert ParameterException("Inter", "DEV/PROP").message == "Inter"


def test_constructor_should_return_parameter_exception_with_provided_parameter_name():
    assert (
        ParameterException("ignored", "DEV/PROP").parameter_name == "DEV/PROP"
    )


def test_constructor_should_return_parameter_exception_with_provided_value_header():
    wanted_value_header: ValueHeader = ValueHeader(
        acq_stamp=10,
        cycle_stamp=14,
        selector=Selectors.NO_SELECTOR,
        update_type=UpdateType.IMMEDIATE_UPDATE,
    )

    exception: ParameterException = ParameterException(
        "Inter", "DEV/PROP", wanted_value_header
    )

    assert exception.header.acq_stamp == 10
    assert exception.header.cycle_stamp == 14
    assert exception.header.selector == Selectors.NO_SELECTOR
    assert exception.header.update_type == UpdateType.IMMEDIATE_UPDATE


def test_constructor_should_return_parameter_exception_with_default_value_header_if_none_provided():
    exception: ParameterException = ParameterException("Inter")
    value_header: ValueHeader = exception.header

    assert value_header.acq_stamp == 0
    assert value_header.cycle_stamp == 0
    assert value_header.selector.selector_id == ""
    assert value_header.update_type == UpdateType.NORMAL


def test_constructor_should_return_exception_with_provided_message():
    assert ParameterException("Inter").message == "Inter"

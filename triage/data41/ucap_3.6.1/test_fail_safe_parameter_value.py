from unittest.mock import Mock

from ucap.common import (
    AcquiredParameterValue,
    FailSafeParameterValue,
    ParameterException,
    ValueHeader,
)


def test_value():
    mock_value = Mock(spec=AcquiredParameterValue)
    fspv = FailSafeParameterValue(mock_value)
    assert fspv.value is mock_value
    assert fspv.exception is None
    assert fspv.header is mock_value.header
    assert fspv.parameter_name is mock_value.parameter_name


def test_exception():
    mock_exception = Mock(spec=ParameterException)
    mock_exception.header = Mock(spec=ValueHeader)
    fspv = FailSafeParameterValue(mock_exception)
    assert fspv.value is None
    assert fspv.exception is mock_exception
    assert fspv.header is mock_exception.header
    assert fspv.parameter_name is mock_exception.parameter_name

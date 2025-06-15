import pytest


def test_can_import_discrete_function_from_value_type():
    try:
        from ucap.common.value_type import DiscreteFunction  # noqa: F401
    except ImportError:
        pytest.fail("Could not import DiscreteFunction from value_type")


def test_can_import_discrete_function_list_from_value_type():
    try:
        from ucap.common.value_type import DiscreteFunctionList  # noqa: F401
    except ImportError:
        pytest.fail("Could not import DiscreteFunctionList from value_type")

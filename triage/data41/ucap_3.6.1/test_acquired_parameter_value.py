from functools import partial
from unittest.mock import Mock

import numpy as np
import pytest

from ucap.common import AcquiredParameterValue, ValueHeader, ValueType

from .utils import (
    inf_values,
    nan_values,
    numeric_array_arguments,
    simple_arguments,
)


def test_getters():
    mock_header = Mock(spec=ValueHeader())
    apv = AcquiredParameterValue("Acquisition", mock_header)
    assert apv.parameter_name == "Acquisition"
    assert apv.header is mock_header


def test_field_names():
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value1", 2, ValueType.LONG)
    apv.update_value("value2", 2.1, ValueType.DOUBLE)
    assert apv.field_names == ("value1", "value2")


def test_values():
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value1", 2, ValueType.LONG)
    apv.update_value("value2", 2.1, ValueType.DOUBLE)
    assert apv.values == {
        "value1": (2, ValueType.LONG),
        "value2": (2.1, ValueType.DOUBLE),
    }


@pytest.mark.parametrize(
    "func_name", ["get_value_and_type", "get_value", "get_type"]
)
def test_should_raise_value_error_if_no_such_field_exist(func_name):
    apv = AcquiredParameterValue("Acquisition")
    with pytest.raises(KeyError):
        getattr(apv, func_name)("Ciao")


def test_update_value_fails_with_new_type():
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value1", 2, ValueType.LONG)
    with pytest.raises(
        TypeError,
        match="Unsupported update: old ValueType is ValueType.LONG, new is ValueType.DOUBLE",
    ):
        apv.update_value("value1", 2.1, ValueType.DOUBLE)


def test_update_value_uses_old_type_if_none():
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value1", 2.1, ValueType.DOUBLE)
    apv.update_value("value1", 2)
    assert apv.values == {
        "value1": (2, ValueType.DOUBLE),
    }


def test_update_value_changes_value():
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value1", 2, ValueType.DOUBLE)
    apv.update_value("value1", 2.1, ValueType.DOUBLE)
    assert apv.values == {
        "value1": (2.1, ValueType.DOUBLE),
    }


@pytest.mark.parametrize(
    "func_name,expected",
    [
        ("get_value_and_type", (10, ValueType.INT)),
        ("get_value", 10),
        ("get_type", ValueType.INT),
    ],
)
def test_should_use_default_field_value_when_no_field_defined(
    func_name, expected
):
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value", 10, ValueType.INT)
    assert getattr(apv, func_name)("value") == expected


@pytest.mark.parametrize("value,value_type", simple_arguments)
def test_get_value_and_type_simple(value, value_type):
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("field1", value, value_type)
    assert apv.get_value_and_type("field1") == (value, value_type)


@pytest.mark.parametrize("value,value_type", numeric_array_arguments)
def test_get_value_and_type_numeric_array(value, value_type):
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("field1", value, value_type)

    output, output_type = apv.get_value_and_type("field1")

    assert output_type == value_type
    assert output is value
    assert not value.flags["WRITEABLE"]


@pytest.mark.parametrize("value,value_type", numeric_array_arguments)
def test_get_value_and_type_numeric_array_makes_numpy_array_from_list(
    value, value_type
):
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("field1", list(value), value_type)

    output = apv._values["field1"].normalized_value
    output_type = apv.get_type("field1")

    assert output_type == value_type
    assert isinstance(output, np.ndarray)
    assert np.array_equal(output, value, equal_nan=True)


@pytest.mark.parametrize("value,value_type", numeric_array_arguments)
def test_get_value_and_type_numeric_array_makes_numpy_array_from_tuple(
    value, value_type
):
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("field1", tuple(value), value_type)

    output = apv._values["field1"].normalized_value
    output_type = apv.get_type("field1")

    assert output_type == value_type
    assert isinstance(output, np.ndarray)
    assert np.array_equal(output, value, equal_nan=True)


def test_get_value_and_type_string():
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value1", "ciao", ValueType.STRING)
    assert apv.get_value_and_type("value1") == ("ciao", ValueType.STRING)


def test_get_value_and_type_string_array():
    apv = AcquiredParameterValue("Acquisition")
    value = ("ciao", "hello")
    apv.update_value("value1", value, ValueType.STRING_ARRAY)

    output, output_type = apv.get_value_and_type("value1")
    assert output_type == ValueType.STRING_ARRAY
    assert output is value


def test_get_value_and_type_string_array_makes_tuple():
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value1", ["ciao", "hello"], ValueType.STRING_ARRAY)

    output = apv._values["value1"].normalized_value
    output_type = apv.get_type("value1")

    assert output == ("ciao", "hello")
    assert output_type == ValueType.STRING_ARRAY


def test_get_value_and_type_string_array_recycles_numpy_array():
    apv = AcquiredParameterValue("Acquisition")
    value = np.array(["ciao", "hello"])
    apv.update_value("value1", value, ValueType.STRING_ARRAY)

    output, output_type = apv.get_value_and_type("value1")
    assert output_type == ValueType.STRING_ARRAY
    assert output is value
    assert not value.flags["WRITEABLE"]


def test_get_value_and_type_string_array_2d():
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value(
        "value1",
        (("ciao", "hello"), ("guten tag", "dober dan")),
        ValueType.STRING_ARRAY_2D,
    )
    assert apv.get_value_and_type("value1") == (
        (("ciao", "hello"), ("guten tag", "dober dan")),
        ValueType.STRING_ARRAY_2D,
    )


def test_get_value_and_type_string_array_2d_makes_tuple():
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value(
        "value1",
        [["ciao", "hello"], ["guten tag", "dober dan"]],
        ValueType.STRING_ARRAY_2D,
    )

    output = apv._values["value1"].normalized_value
    output_type = apv.get_type("value1")

    assert output == (("ciao", "hello"), ("guten tag", "dober dan"))
    assert output_type == ValueType.STRING_ARRAY_2D


def test_get_value_and_type_string_array_2d_recycles_numpy_array():
    apv = AcquiredParameterValue("Acquisition")
    value = np.array([["ciao", "hello"], ["guten tag", "dober dan"]])
    apv.update_value("value1", value, ValueType.STRING_ARRAY_2D)

    output, output_type = apv.get_value_and_type("value1")
    assert output_type == ValueType.STRING_ARRAY_2D
    assert output is value
    assert not value.flags["WRITEABLE"]


def test_update_value_raises_for_none_int():
    apv = AcquiredParameterValue("DEV/PROP")

    with pytest.raises(
        TypeError,
    ):
        apv.update_value(
            field_name="value", value=None, value_type=ValueType.INT
        )


def test_update_value_raises_for_none_and_none_value_type():
    apv = AcquiredParameterValue("DEV/PROP")

    with pytest.raises(
        Exception, match="ValueType for .*None.* could not be inferred"
    ):
        apv.update_value(field_name="value", value=None, value_type=None)


def test_update_value_raises_for_dict():
    apv = AcquiredParameterValue("DEV/PROP")

    with pytest.raises(
        TypeError, match="ValueType for .*dict.* could not be inferred"
    ):
        apv.update_value("value", {})


@pytest.mark.parametrize(
    "value,value_types",
    [
        (
            int(np.iinfo(np.int8).max) + 1,
            (ValueType.BYTE, ValueType.BYTE_ARRAY, ValueType.BYTE_ARRAY_2D),
        ),
        (
            int(np.iinfo(np.int16).max) + 1,
            (ValueType.SHORT, ValueType.SHORT_ARRAY, ValueType.SHORT_ARRAY_2D),
        ),
        (
            int(np.iinfo(np.int32).max) + 1,
            (ValueType.INT, ValueType.INT_ARRAY, ValueType.INT_ARRAY_2D),
        ),
        (
            int(np.iinfo(np.int64).max) + 1,
            (ValueType.LONG, ValueType.LONG_ARRAY, ValueType.LONG_ARRAY_2D),
        ),
    ],
)
def test_overflow(value, value_types):
    apv = AcquiredParameterValue("Acquisition")
    for value_type in value_types:
        with pytest.raises(OverflowError):
            apv.update_value("field1", value, value_type)

        value = [value]


@pytest.mark.parametrize("nan_value", nan_values)
@pytest.mark.parametrize(
    "int_type", [ValueType.BYTE, ValueType.SHORT, ValueType.INT, ValueType.LONG]
)
def test_int_nan(nan_value, int_type):
    apv = AcquiredParameterValue("Acquisition")

    with pytest.raises(ValueError, match="cannot convert float NaN to integer"):
        apv.update_value("value", nan_value, int_type)


@pytest.mark.parametrize("nan_value", nan_values)
@pytest.mark.parametrize(
    "int_type",
    [
        ValueType.BYTE_ARRAY,
        ValueType.SHORT_ARRAY,
        ValueType.INT_ARRAY,
        ValueType.LONG_ARRAY,
    ],
)
def test_int_array_nan(nan_value, int_type):
    apv = AcquiredParameterValue("Acquisition")

    with pytest.raises(ValueError, match="cannot convert float NaN to integer"):
        apv.update_value("value", [nan_value], int_type)


@pytest.mark.parametrize("nan_value", nan_values)
@pytest.mark.parametrize(
    "int_type",
    [
        ValueType.BYTE_ARRAY_2D,
        ValueType.SHORT_ARRAY_2D,
        ValueType.INT_ARRAY_2D,
        ValueType.LONG_ARRAY_2D,
    ],
)
def test_int_array_2d_nan(nan_value, int_type):
    apv = AcquiredParameterValue("Acquisition")

    with pytest.raises(ValueError, match="cannot convert float NaN to integer"):
        apv.update_value("value", [[nan_value]], int_type)


@pytest.mark.parametrize("nan_value", nan_values)
@pytest.mark.parametrize(
    "array_func", [list, tuple, partial(np.array, dtype=np.float32)]
)
def test_float_nan(nan_value, array_func):
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value", nan_value, ValueType.FLOAT)
    apv.update_value("value[]", array_func([nan_value]), ValueType.FLOAT_ARRAY)
    apv.update_value(
        "value[][]", array_func([[nan_value]]), ValueType.FLOAT_ARRAY_2D
    )

    output_value = apv._values["value"].normalized_value
    output_type = apv.get_type("value")

    assert output_type == ValueType.FLOAT
    assert output_value.dtype == np.float32
    assert np.array_equal(
        output_value, np.array(nan_value, dtype=np.float32), equal_nan=True
    )

    output_value_array = apv._values["value[]"].normalized_value
    output_type_array = apv.get_type("value[]")

    assert output_type_array == ValueType.FLOAT_ARRAY
    assert output_value_array.dtype == np.float32
    assert np.array_equal(
        output_value_array,
        np.array([nan_value], dtype=np.float32),
        equal_nan=True,
    )

    output_value_array_2d = apv._values["value[][]"].normalized_value
    output_type_array_2d = apv.get_type("value[][]")

    assert output_type_array_2d == ValueType.FLOAT_ARRAY_2D
    assert output_value_array_2d.dtype == np.float32
    assert np.array_equal(
        output_value_array_2d,
        np.array([[nan_value]], dtype=np.float32),
        equal_nan=True,
    )


@pytest.mark.parametrize("nan_value", nan_values)
@pytest.mark.parametrize(
    "array_func", [list, tuple, partial(np.array, dtype=np.float64)]
)
def test_double_nan(nan_value, array_func):
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value", nan_value, ValueType.DOUBLE)
    apv.update_value("value[]", array_func([nan_value]), ValueType.DOUBLE_ARRAY)
    apv.update_value(
        "value[][]", array_func([[nan_value]]), ValueType.DOUBLE_ARRAY_2D
    )

    output_value = apv._values["value"].normalized_value
    output_type = apv.get_type("value")

    assert output_type == ValueType.DOUBLE
    assert output_value.dtype == np.float64
    assert np.array_equal(
        output_value, np.array(nan_value, dtype=np.float64), equal_nan=True
    )

    output_value_array = apv._values["value[]"].normalized_value
    output_type_array = apv.get_type("value[]")

    assert output_type_array == ValueType.DOUBLE_ARRAY
    assert output_value_array.dtype == np.float64
    assert np.array_equal(
        output_value_array,
        np.array([nan_value], dtype=np.float64),
        equal_nan=True,
    )

    output_value_array_2d = apv._values["value[][]"].normalized_value
    output_type_array_2d = apv.get_type("value[][]")

    assert output_type_array_2d == ValueType.DOUBLE_ARRAY_2D
    assert output_value_array_2d.dtype == np.float64
    assert np.array_equal(
        output_value_array_2d,
        np.array([[nan_value]], dtype=np.float64),
        equal_nan=True,
    )


@pytest.mark.parametrize("inf_value", inf_values)
@pytest.mark.parametrize(
    "int_type", [ValueType.BYTE, ValueType.SHORT, ValueType.INT, ValueType.LONG]
)
def test_int_inf(inf_value, int_type):
    apv = AcquiredParameterValue("Acquisition")

    with pytest.raises(OverflowError):
        apv.update_value("value", inf_value, int_type)


@pytest.mark.parametrize("inf_value", inf_values)
@pytest.mark.parametrize(
    "int_type",
    [
        ValueType.BYTE_ARRAY,
        ValueType.SHORT_ARRAY,
        ValueType.INT_ARRAY,
        ValueType.LONG_ARRAY,
    ],
)
def test_int_array_inf(inf_value, int_type):
    apv = AcquiredParameterValue("Acquisition")

    with pytest.raises(OverflowError):
        apv.update_value("value", [inf_value], int_type)


@pytest.mark.parametrize("inf_value", inf_values)
@pytest.mark.parametrize(
    "int_type",
    [
        ValueType.BYTE_ARRAY_2D,
        ValueType.SHORT_ARRAY_2D,
        ValueType.INT_ARRAY_2D,
        ValueType.LONG_ARRAY_2D,
    ],
)
def test_int_array_2d_inf(inf_value, int_type):
    apv = AcquiredParameterValue("Acquisition")

    with pytest.raises(OverflowError):
        apv.update_value("value", [[inf_value]], int_type)


@pytest.mark.parametrize("inf_value", inf_values)
@pytest.mark.parametrize(
    "array_func", [list, tuple, partial(np.array, dtype=np.float32)]
)
def test_float_inf(inf_value, array_func):
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value", inf_value, ValueType.FLOAT)
    apv.update_value("value[]", array_func([inf_value]), ValueType.FLOAT_ARRAY)
    apv.update_value(
        "value[][]", array_func([[inf_value]]), ValueType.FLOAT_ARRAY_2D
    )

    output_value = apv._values["value"].normalized_value
    output_type = apv.get_type("value")

    assert output_type == ValueType.FLOAT
    assert output_value.dtype == np.float32
    assert np.array_equal(output_value, np.array(inf_value, dtype=np.float32))

    output_value_array = apv._values["value[]"].normalized_value
    output_type_array = apv.get_type("value[]")

    assert output_type_array == ValueType.FLOAT_ARRAY
    assert output_value_array.dtype == np.float32
    assert np.array_equal(
        output_value_array, np.array([inf_value], dtype=np.float32)
    )

    output_value_array_2d = apv._values["value[][]"].normalized_value
    output_type_array_2d = apv.get_type("value[][]")

    assert output_type_array_2d == ValueType.FLOAT_ARRAY_2D
    assert output_value_array_2d.dtype == np.float32
    assert np.array_equal(
        output_value_array_2d, np.array([[inf_value]], dtype=np.float32)
    )


@pytest.mark.parametrize("inf_value", inf_values)
@pytest.mark.parametrize(
    "array_func", [list, tuple, partial(np.array, dtype=np.float64)]
)
def test_double_inf(inf_value, array_func):
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value", inf_value, ValueType.DOUBLE)
    apv.update_value("value[]", array_func([inf_value]), ValueType.DOUBLE_ARRAY)
    apv.update_value(
        "value[][]", array_func([[inf_value]]), ValueType.DOUBLE_ARRAY_2D
    )

    output_value = apv._values["value"].normalized_value
    output_type = apv.get_type("value")

    assert output_type == ValueType.DOUBLE
    assert output_value.dtype == np.float64
    assert np.array_equal(output_value, np.array(inf_value, dtype=np.float64))

    output_value_array = apv._values["value[]"].normalized_value
    output_type_array = apv.get_type("value[]")

    assert output_type_array == ValueType.DOUBLE_ARRAY
    assert output_value_array.dtype == np.float64
    assert np.array_equal(
        output_value_array, np.array([inf_value], dtype=np.float64)
    )

    output_value_array_2d = apv._values["value[][]"].normalized_value
    output_type_array_2d = apv.get_type("value[][]")

    assert output_type_array_2d == ValueType.DOUBLE_ARRAY_2D
    assert output_value_array_2d.dtype == np.float64
    assert np.array_equal(
        output_value_array_2d, np.array([[inf_value]], dtype=np.float64)
    )


@pytest.mark.parametrize(
    "value,wrong_value_type",
    [
        # 0D
        (1, ValueType.INT_ARRAY),
        (1, ValueType.INT_ARRAY_2D),
        (np.array(1.2), ValueType.DOUBLE_ARRAY),
        (np.array(1.2), ValueType.DOUBLE_ARRAY_2D),
        # 1D
        ([1, 2, 3], ValueType.INT),
        ([1, 2, 3], ValueType.INT_ARRAY_2D),
        (np.array((1.1, 2, 3)), ValueType.DOUBLE_ARRAY_2D),
        (np.array((1.1, 2, 3)), ValueType.DOUBLE),
        # 2D
        ([[1, 2, 3]], ValueType.DOUBLE),
        ([[1, 2, 3]], ValueType.DOUBLE_ARRAY),
        (np.array([[1, 2, 3.2]]), ValueType.DOUBLE),
        (np.array([[1, 2, 3.2]]), ValueType.DOUBLE_ARRAY),
    ],
)
def test_wrong_shape(value, wrong_value_type):
    apv = AcquiredParameterValue("Acquisition")
    with pytest.raises(
        ValueError,
        match=f"Expected {wrong_value_type.value.number_of_dimensions}D value, got {np.array(value).ndim}",
    ):
        apv.update_value("value1", value, wrong_value_type)


def test_not_1d_string_array():
    apv = AcquiredParameterValue("Acquisition")
    with pytest.raises(
        TypeError, match="The sequence contains non-string values"
    ):
        apv.update_value(
            "value1", [["ciao", "dober dan"]], ValueType.STRING_ARRAY
        )


@pytest.mark.parametrize(
    "value",
    [
        ("ciao", ("dober dan", "hello")),
        (("dober dan", "hello"), "ciao"),
    ],
)
def test_malformed_string_matrix(value):
    apv = AcquiredParameterValue("Acquisition")
    with pytest.raises(
        TypeError,
        match="Expected 2D string sequence, .*",
    ) as exc:
        apv.update_value("value1", value, ValueType.STRING_ARRAY_2D)
    assert isinstance(exc.value.__cause__, TypeError)
    assert str(exc.value.__cause__) == f"Expected 1D string sequence, got {str}"


@pytest.mark.parametrize(
    "value",
    [
        (("ciao",), ("dober dan", "hello")),
        (("dober dan", "hello"), ("ciao",)),
    ],
)
def test_string_matrix_inhomogeneous_rows(value):
    apv = AcquiredParameterValue("Acquisition")
    with pytest.raises(
        ValueError,
        match="Expected 2D string sequence, but rows have different sizes",
    ):
        apv.update_value("value1", value, ValueType.STRING_ARRAY_2D)


def test_none_integer():
    apv = AcquiredParameterValue("Acquisition")
    with pytest.raises(TypeError, match=".* not 'NoneType'"):
        apv.update_value("value1", None, ValueType.BYTE)


def test_none_integer_1d():
    apv = AcquiredParameterValue("Acquisition")
    with pytest.raises(TypeError, match=".* not 'NoneType'"):
        apv.update_value("value1", [None, 1, 2, 3], ValueType.INT_ARRAY)


def test_none_integer_2d():
    apv = AcquiredParameterValue("Acquisition")
    with pytest.raises(TypeError, match=".* not 'NoneType'"):
        apv.update_value(
            "value1", [[1, 2, None], [4, 5, 6]], ValueType.SHORT_ARRAY_2D
        )


def test_none_string():
    apv = AcquiredParameterValue("Acquisition")
    with pytest.raises(TypeError, match="Expected string, got .*None.*"):
        apv.update_value("value1", None, ValueType.STRING)
    with pytest.raises(
        TypeError, match="The sequence contains non-string values"
    ):
        apv.update_value("value1", ["ciao", None], ValueType.STRING_ARRAY)
    with pytest.raises(
        TypeError, match="Expected 2D string sequence, .*"
    ) as exc_2d:
        apv.update_value("value1", [["ciao", None]], ValueType.STRING_ARRAY_2D)
    assert (
        str(exc_2d.value.__cause__) == "The sequence contains non-string values"
    )


def test_none_boolean():
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value1", None, ValueType.BOOLEAN)
    assert bool(apv.get_value("value1")) is False


def test_none_float():
    apv = AcquiredParameterValue("Acquisition")

    apv.update_value("value1", None, ValueType.FLOAT)
    assert np.isnan(apv._values["value1"].normalized_value)

    apv.update_value("value2", [None, 1, 2.2, 3], ValueType.FLOAT_ARRAY)
    assert np.array_equal(
        apv._values["value2"].normalized_value,
        np.array([np.nan, 1.0, 2.2, 3.0], dtype=np.float32),
        equal_nan=True,
    )

    apv.update_value("value3", [[None, 1, 2.2, 3]], ValueType.FLOAT_ARRAY_2D)
    assert np.array_equal(
        apv._values["value3"].normalized_value,
        np.array([[np.nan, 1, 2.2, 3]], dtype=np.float32),
        equal_nan=True,
    )


def test_none_double():
    apv = AcquiredParameterValue("Acquisition")

    apv.update_value("value1", None, ValueType.DOUBLE)
    assert np.isnan(apv._values["value1"].normalized_value)

    apv.update_value("value2", [None, 1, 2.2, 3], ValueType.DOUBLE_ARRAY)
    assert np.array_equal(
        apv._values["value2"].normalized_value,
        np.array([np.nan, 1.0, 2.2, 3.0], dtype=np.float64),
        equal_nan=True,
    )

    apv.update_value("value3", [[None, 1, 2.2, 3]], ValueType.DOUBLE_ARRAY_2D)
    assert np.array_equal(
        apv._values["value3"].normalized_value,
        np.array([[np.nan, 1, 2.2, 3]], dtype=np.float64),
        equal_nan=True,
    )


# ValueType inference


@pytest.mark.parametrize("value", (True, np.bool_(True)))  # noqa: FBT003, PT007
def test_bool_type_inference(value):
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value", value)
    assert apv.values["value"][1] == ValueType.BOOLEAN


def test_bool_array_type_inference():
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value", np.array((True, True, False)))
    assert apv.values["value"][1] == ValueType.BOOLEAN_ARRAY


@pytest.mark.parametrize("value,value_type", numeric_array_arguments)
def test_japc_value_type_inference(value, value_type):
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("field1", list(value), value_type.value.japc_value_type)

    output, output_type = apv.get_value_and_type("field1")

    assert output_type == value_type
    assert np.array_equal(output, value, equal_nan=True)


@pytest.mark.parametrize("value", [3, 255, 10000000])
def test_update_value_int_default_type(value: int):
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value1", value)

    # For retro-compatibility
    assert apv.get_type("value1") == ValueType.INT


def test_update_value_float_default_type():
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value1", 20.1)

    # For retro-compatibility
    assert apv.get_type("value1") == ValueType.DOUBLE


@pytest.mark.parametrize(
    "value,value_type",
    [
        ("ciao", ValueType.STRING),
        (np.array("ciao"), ValueType.STRING),
        (np.array(["ciao"]), ValueType.STRING_ARRAY),
        (np.array([["ciao"]]), ValueType.STRING_ARRAY_2D),
        *numeric_array_arguments,
    ],
)
def test_update_value_type_inference_numpy(value, value_type):
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value1", value)

    assert apv.get_type("value1") == value_type


@pytest.mark.parametrize(
    "value",
    [
        ["ciao"],
        ("ciao",),
        [["ciao"]],
        (("ciao",),),
        [1],
        (10.2,),
        [[1, 2, 3]],
        ((1, 2, 3), (4, 5, 6)),
    ],
)
def test_no_inference_for_python_iterables(value):
    apv = AcquiredParameterValue("Acquisition")
    with pytest.raises(
        TypeError, match=f"ValueType for {type(value)} could not be inferred"
    ):
        apv.update_value("value1", value)


def test_get_value_with_type():
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value2", 3, ValueType.INT)
    assert (
        apv.get_value_with_type(field_name="value2", value_type=ValueType.INT)
        == 3
    )


def test_get_value_with_type_throws():
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value2", 3, ValueType.INT)
    with pytest.raises(
        TypeError,
        match="Expected ValueType.DISCRETE_FUNCTION, got ValueType.INT",
    ):
        apv.get_value_with_type(
            field_name="value2", value_type=ValueType.DISCRETE_FUNCTION
        )


def test_validation_is_transparent():
    # Given
    np.seterr(divide="ignore", over="log")
    np._set_promotion_state("weak_and_warn")

    # When
    apv = AcquiredParameterValue("Acquisition")
    value = np.array([1, 2, 3])
    apv.update_value("value1", value, ValueType.LONG_ARRAY)

    # Then
    assert np.geterr()["divide"] == "ignore"
    assert np.geterr()["over"] == "log"
    assert np._get_promotion_state() == "weak_and_warn"


@pytest.mark.parametrize(
    "value,expected",
    [
        (np.int8(1), ValueType.BYTE),
        (np.int16(1), ValueType.SHORT),
        (np.int32(1), ValueType.INT),
        (np.int64(1), ValueType.LONG),
        (np.float32(1.0), ValueType.FLOAT),
        (np.float64(1.0), ValueType.DOUBLE),
    ],
)
def test_infer_numpy_scalar_types(value, expected):
    apv = AcquiredParameterValue("Acquisition")
    apv.update_value("value", value)
    assert apv.values["value"][1] == expected


@pytest.mark.parametrize(
    "source,target",
    [
        (ValueType.INT_ARRAY, ValueType.LONG_ARRAY),
        (ValueType.FLOAT_ARRAY, ValueType.DOUBLE_ARRAY),
    ],
)
def test_automatic_cast(source, target):
    # Given
    apv = AcquiredParameterValue("Acquisition")
    array = np.array([1, 2, 3], dtype=source.value.numpy_dtype)

    # When
    apv.update_value("value", array, target)

    # Then
    assert (
        apv._values["value"].normalized_value.dtype == target.value.numpy_dtype
    )
    assert apv.get_type("value") == target


@pytest.mark.parametrize(
    "source,target",
    [
        (ValueType.LONG_ARRAY, ValueType.INT_ARRAY),
        (ValueType.DOUBLE_ARRAY, ValueType.FLOAT_ARRAY),
    ],
)
def test_automatic_cast_failure(source, target):
    apv = AcquiredParameterValue("Acquisition")
    array = np.array([1, 2, 3], dtype=source.value.numpy_dtype)

    with pytest.raises(TypeError):
        apv.update_value("value", array, target)


def test_original_value():
    # Given
    apv = AcquiredParameterValue("Acquisition")

    # When
    apv.update_value("value", 10, ValueType.SHORT)

    # Then
    assert isinstance(apv.get_value("value"), int)

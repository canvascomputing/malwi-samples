import math

import numpy as np
import pytest

from ucap.common.discrete_function import DiscreteFunction


def test_init_copies_parameters():
    x = [1, 2]
    y = [4, 5]

    discrete_function = DiscreteFunction(x, y)

    x.append(3)
    y.append(6)

    np.testing.assert_array_equal((1, 2), discrete_function.x)
    np.testing.assert_array_equal((4, 5), discrete_function.y)


def test_init_should_raise_exception_if_different_size():
    x = [1, 2, 3]
    y = [1, 2]

    with pytest.raises(
        ValueError, match="X array length does not match Y array"
    ):
        DiscreteFunction(x, y)


def test_get_x():
    x = [1, 2, 3, math.nan]
    y = [4, 5, 6, math.nan]

    discrete_function = DiscreteFunction(x, y)

    np.testing.assert_array_equal(x, discrete_function.x)


def test_get_y():
    x = [1, 2, 3, math.nan]
    y = [4, 5, 6, math.nan]

    discrete_function = DiscreteFunction(x, y)

    np.testing.assert_array_equal(y, discrete_function.y)


def test_get_x_numpy():
    x = np.array((1, 2, 3, math.nan))
    y = np.array((4, 5, 6, math.nan))

    discrete_function = DiscreteFunction(x, y)

    assert x is discrete_function.x
    assert not x.flags["WRITEABLE"]


def test_get_y_numpy():
    x = np.array((1, 2, 3, math.nan))
    y = np.array((4, 5, 6, math.nan))

    discrete_function = DiscreteFunction(x, y)

    assert y is discrete_function.y
    assert not y.flags["WRITEABLE"]


def test_getitem():
    x = [1, 2, 3, math.nan]
    y = [4, 5, 6, math.nan]

    discrete_function = DiscreteFunction(x, y)

    np.testing.assert_array_equal((2, 5), discrete_function[1])


def test_getitem_negative_index():
    x = [1, 2, 3, math.nan]
    y = [4, 5, 6, math.nan]

    discrete_function = DiscreteFunction(x, y)

    np.testing.assert_array_equal((3, 6), discrete_function[-2])


def test_iter():
    # no explicit implementation needed
    x = [1, 2, 3, math.nan]
    y = [4, 5, 6, math.nan]

    discrete_function = DiscreteFunction(x, y)

    np.testing.assert_array_equal(
        [(1, 4), (2, 5), (3, 6), (math.nan, math.nan)], list(discrete_function)
    )


def test_len():
    x = [1, 2, 3, math.nan]
    y = [4, 5, 6, math.nan]

    discrete_function = DiscreteFunction(x, y)

    assert len(discrete_function) == 4


def test_eq():
    x = [1, 2, 3, math.nan]
    y = [4, 5, 6, math.nan]

    discrete_function1 = DiscreteFunction(x, y)
    discrete_function2 = DiscreteFunction(x, y)

    assert discrete_function1 == discrete_function2


def test_ne():
    x = [1, 2, 3, math.nan]
    y = [4, 5, 6, math.nan]

    discrete_function1 = DiscreteFunction(x, y)
    discrete_function2 = DiscreteFunction(x, x)

    assert discrete_function1 != discrete_function2


def test_str():
    x = [1, 2, 3, math.nan]
    y = [4, 5, 6, math.nan]

    discrete_function = DiscreteFunction(x, y)

    assert (
        str(discrete_function)
        == "DiscreteFunction(x=[ 1.  2.  3. nan], y=[ 4.  5.  6. nan])"
    )


def test_set_x_fails():
    x = [1, 2, 3]
    y = [4, 5, 6]

    discrete_function = DiscreteFunction(x, y)

    with pytest.raises(AttributeError):
        discrete_function.x = y


def test_set_y_fails():
    x = [1, 2, 3]
    y = [4, 5, 6]

    discrete_function = DiscreteFunction(x, y)

    with pytest.raises(AttributeError):
        discrete_function.y = x

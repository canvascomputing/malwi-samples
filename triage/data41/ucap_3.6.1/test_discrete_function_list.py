import pytest

from ucap.common import DiscreteFunction, DiscreteFunctionList

x_a = [1.0, 2.0, 3.0]
y_a = [4.0, 5.0, 6.0]
x_b = [1.0, 2.0, 4.0]
y_b = [7.0, 8.0, 9.0]


def test_init_none():
    with pytest.raises(TypeError):
        DiscreteFunctionList(None)


def test_functions_should_return_functions():
    discrete_function_a = DiscreteFunction(x_a, y_a)
    discrete_function_b = DiscreteFunction(x_b, y_b)

    dfl = DiscreteFunctionList([discrete_function_a, discrete_function_b])

    assert (discrete_function_a, discrete_function_b) == dfl.functions


def test_len_should_return_length():
    discrete_function_a = DiscreteFunction(x_a, y_a)
    discrete_function_b = DiscreteFunction(x_b, y_b)

    dfl = DiscreteFunctionList([discrete_function_a, discrete_function_b])

    assert len(dfl) == 2


def test_getitem_should_return_function():
    discrete_function_a = DiscreteFunction(x_a, y_a)
    discrete_function_b = DiscreteFunction(x_b, y_b)

    dfl = DiscreteFunctionList([discrete_function_a, discrete_function_b])

    assert discrete_function_a == dfl[0]
    assert id(discrete_function_a) == id(dfl[0])
    assert discrete_function_b == dfl[1]
    assert id(discrete_function_b) == id(dfl[1])


def test_getitem_should_raise_exception_if_wrong_index():
    discrete_function_a = DiscreteFunction(x_a, y_a)
    discrete_function_b = DiscreteFunction(x_b, y_b)

    dfl = DiscreteFunctionList([discrete_function_a, discrete_function_b])

    with pytest.raises(IndexError):
        dfl[1908]


def test_iter():
    # no explicit implementation needed
    discrete_function_a = DiscreteFunction(x_a, y_a)
    discrete_function_b = DiscreteFunction(x_b, y_b)

    dfl = DiscreteFunctionList([discrete_function_a, discrete_function_b])

    assert [discrete_function_a, discrete_function_b] == list(dfl)


def test_functions_should_create_a_shallow_copy():
    discrete_function_a = DiscreteFunction(x_a, y_a)
    functions = [discrete_function_a]
    dfl = DiscreteFunctionList(functions)

    functions_copy = dfl.functions

    assert functions_copy == tuple(functions)
    assert id(functions_copy) != id(functions)
    assert id(functions_copy[0]) == id(discrete_function_a)


def test_eq():
    df1a = DiscreteFunction(x_a, y_a)
    df1b = DiscreteFunction(x_b, y_b)
    df2a = DiscreteFunction(x_a, y_a)
    df2b = DiscreteFunction(x_b, y_b)

    dfl1 = DiscreteFunctionList([df1a, df1b])
    dfl2 = DiscreteFunctionList([df2a, df2b])

    assert dfl1 == dfl2


def test_ne():
    df1a = DiscreteFunction(x_a, y_a)
    df1b = DiscreteFunction(x_b, y_b)
    df2a = DiscreteFunction(x_a, y_a)

    dfl1 = DiscreteFunctionList([df1a, df1b])
    dfl2 = DiscreteFunctionList([df2a])

    assert dfl1 != dfl2


def test_str():
    discrete_function_a = DiscreteFunction(x_a, y_a)

    dfl = DiscreteFunctionList([discrete_function_a])

    assert (
        str(dfl)
        == "DiscreteFunctionList(functions=(DiscreteFunction(x=[1. 2. 3.], y=[4. 5. 6.]),))"
    )

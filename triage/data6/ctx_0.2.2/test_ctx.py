import pytest
from ctx import Ctx


def test_lookup_error():
    """Should  return LookupError if no attiibute or key is found"""
    with pytest.raises(LookupError):
        x = Ctx()
        (x.no_key == 5)
    with pytest.raises(LookupError):
        x = Ctx()
        (x['no_key'] == 5)


def test_attribute_error():
    """Should raise AttributeError if attempt to set an attribute."""
    with pytest.raises(AttributeError):
        x = Ctx()
        x.copy = 5


def test_attribue_access():
    """Should return attribute of an object."""

    x = Ctx()
    assert x.__doc__ == x["__doc__"]


def test_init():
    """Should initialize an object with keywords"""
    p = {}
    q = {}

    x = Ctx(a=p, b=q)
    assert x['a'] is p
    assert x.a is p
    assert x['b'] is q
    assert x.b is q


def test_item():
    """Should set an item with ctx['a'] and retrieve it with ctx[a] or ctx.a"""
    p = {}
    x = Ctx()
    x['a'] = p
    assert x.a is p
    assert x['a'] is p


def test_attr():
    """Should set an item with ctx.a and retrieve it with ctx[a] or ctx.a"""

    p = {}
    x = Ctx()
    x.a = p
    assert x.a is p
    assert x['a'] is p


def test_init_copy():
    """Should create a shallow copy."""

    p = {}
    q = {}

    x = Ctx(a=p, b=q)
    y = x.copy()
    assert x is not y
    assert y['a'] is p
    assert y.a is p
    assert y['b'] is q
    assert y.b is q


if __name__ == '__main__':
    pytest.main()

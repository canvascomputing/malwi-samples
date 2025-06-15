import pytest

from ucap.common import Selector


@pytest.fixture()
def selector_zero():
    return Selector("PSB.USER.ZERO")


def test_id(selector_zero):
    assert selector_zero.selector_id == "PSB.USER.ZERO"


def test_str(selector_zero):
    assert str(selector_zero) == "Selector(selector_id=PSB.USER.ZERO)"


def test_eq(selector_zero):
    assert selector_zero == Selector("PSB.USER.ZERO")


def test_ne(selector_zero):
    selector2 = Selector("PSB.USER.MD1")

    assert selector_zero != selector2

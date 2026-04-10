from calculator import add, subtract, multiply, divide


def test_add_positivenumbers():
    assert add(2, 3) == 5


def test_add_negativenumbers():
    assert add(-2, -3) == -5


def test_subtract():
    assert subtract(5, 2) == 3


def test_subtract_negative():
    assert subtract(-5, -2) == -3


def test_subtract_mixed():
    assert subtract(5, -2) == 7


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(6, 2) == 3

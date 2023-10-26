import pytest

import Source.FirstDemo as functions


def test_add():
    result = functions.add(1, 2)

    # Assert will continue execution if test passes, else halts execution
    # assert result == 3

    # FAILED Test/FirstDemo_Test.py::test_add - assert 3 == 6
    assert result == 6


def test_divide():
    result = functions.divide(10, 3)

    # FAILED Test/FirstDemo_Test.py::test_divide - assert 3.3333333333333335 == 3.3
    assert result == 3.3


def test_divide_by_0():
    # with pytest.raises(ZeroDivisionError):

    with pytest.raises(ValueError):
        # Below are without pytest.raises(...
        # FAILED Test/FirstDemo_Test.py::test_divide_by_0 - ZeroDivisionError: division by zero
        result = functions.divide(10, 0)
        # E       ZeroDivisionError: division by zero

        assert True


def test_add_string():
    result = functions.add("I like ", "pizzas")
    assert result == "I like pizzas"

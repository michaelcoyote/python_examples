import pytest

# content of test_sample.py
# all about some pytest examples here


def func(x):
    """Function suitable for testing."""
    if isinstance(x, int):
        return x + 1
    else:
        raise TypeError("x should be an integer")


def sqrrt(x):
    """Square root function suitable for testing."""
    if isinstance(x, int):
        return x * x
    else:
        raise TypeError("x should be an integer")


# Start the tests here
# Using @pytest.mark decorators to perform tests in specific ways
@pytest.mark.parametrize("i, output", [(3, 4), (5, 6), (11, 12)])
def test_func_answer(i, output):
    """Test with parametrized inputs and outputs."""
    assert func(i) == output


def test_func_bad_type():
    """Test catching raised TypeError"""
    with pytest.raises(TypeError):
        func("badinput")


@pytest.mark.parametrize("i, output", [(3, 9), (5, 25), (11, 121)])
def test_sqrrt_answer(i, output):
    """Test with parametrized inputs and outputs."""
    assert sqrrt(i) == output


def test_sqrrt_bad_type():
    """Test catching raised TypeError"""
    with pytest.raises(TypeError):
        sqrrt("badinput")


@pytest.mark.skip(reason="This is a test to be skipped")
def test_skip_me():
    """Test with a skip."""
    assert(True)

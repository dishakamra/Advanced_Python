from math_utils import add, div, area_of_circle
import pytest

def test_add_two_nos():
    assert add(2,3) == 5

def test_divide_nos():
    assert div(10,2) == 5

# plain assert
def test_plan_assert():
    x = 10
    assert x > 5

# checking exceptions
def test_raises():
    with pytest.raises(ValueError) as excinfo:
        int("not-a-number")
        assert "invalid literal" in str(excinfo.value)

# Approximate float comparison
def test_area_float():
    assert area_of_circle(1) == pytest.approx(3.14159265)

@pytest.fixture
def sample_list():
    print("\n[setup] create list")
    return [1, 2, 3]

def test_sum(sample_list):
    assert sum(sample_list) == 6 # uses the list from the fixture

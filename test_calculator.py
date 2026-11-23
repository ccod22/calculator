import pytest
from calculator import add, subtract, multiply, divide
def test_add():
	assert add(5,3) == 8
def test_subtract():
	assert_subtract(10,4) == 6
def test_multiply():
	assert_multiply(4,5) == 20
def test_divide():
	assert_divide(10,2) == 5
def test_divide_zero():
	with pytest.raises(ValueError):
	divide(10,0)
from fizzbuzz import fizzbuzz
import pytest

def check_fizzbuzz(value, expected_value):
    ret_val = fizzbuzz(value)
    assert ret_val == expected_value

def test_return_1_when_passed_1():
    check_fizzbuzz(1, "1")

def test_return_2_when_passed_2():
    check_fizzbuzz(2, "2")
from fizzbuzz import fizzbuzz
import pytest

def test_fizzbuzz_is_callable():
    fizzbuzz(1)

def test_return_1_when_passed_1():
    ret_val = fizzbuzz(1)
    assert ret_val == "1"
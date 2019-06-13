from fizzbuzz import fizzbuzz
import pytest

def check_fizzbuzz(value, expected_value):
    ret_val = fizzbuzz(value)
    assert ret_val == expected_value

def test_return_1_when_passed_1():
    check_fizzbuzz(1, "1")

def test_return_2_when_passed_2():
    check_fizzbuzz(2, "2")

def test_return_fizz_when_passed_3():
    check_fizzbuzz(3, "Fizz")

def test_return_buzz_when_passed_5():
    check_fizzbuzz(5, "Buzz")

def test_return_fizz_when_passed_6():
    check_fizzbuzz(6, "Fizz")

def test_return_buzz_when_passed_10():
    check_fizzbuzz(10, "Buzz")

def test_return_fizzbuzz_when_passed_15():
    check_fizzbuzz(15, "FizzBuzz")

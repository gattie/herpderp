import pytest
from herpderp import herpderp as hd

def check_herpderp(value, expected_value):
    ret_val = hd.herpderp(value)
    assert ret_val == expected_value

def test_return_1_when_passed_1():
    check_herpderp(1, "1")

def test_return_2_when_passed_2():
    check_herpderp(2, "2")

def test_return_fizz_when_passed_3():
    check_herpderp(3, "Herp")

def test_return_buzz_when_passed_5():
    check_herpderp(5, "Derp")

def test_return_fizz_when_passed_6():
    check_herpderp(6, "Herp")

def test_return_buzz_when_passed_10():
    check_herpderp(10, "Derp")

def test_return_herpderp_when_passed_15():
    check_herpderp(15, "HerpDerp")

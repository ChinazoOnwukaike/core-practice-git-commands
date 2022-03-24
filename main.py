import pytest


def always_returns_true():
    return True

def example_func():
    return "This is an example function. Poppy make change to this function again "

def test_always_returns_true():
    assert always_returns_true()

def poppy_function():
    print("Hi this is Poppy")


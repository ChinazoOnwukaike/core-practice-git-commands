import pytest


def always_returns_true():
<<<<<<< HEAD
    return None
=======
    return True
>>>>>>> 041961a750efac700c991b6ff58a823151a4bfd2

def example_func():
    return "This is an example function."

def test_always_returns_true():
    assert always_returns_true()

def poppy_function():
    print("Hi this is Poppy")


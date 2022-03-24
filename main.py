import pytest


def always_returns_true():
    return True

def example_func():
    return "This is an example function."

def test_always_returns_true():
    assert always_returns_true()

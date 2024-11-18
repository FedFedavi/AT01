import pytest
from main2 import is_palindrom


def test_is_palindrom_true():
    assert is_palindrom('madam') == True


def test_is_palindrom_false():
    assert is_palindrom('hello') == False


@pytest.mark.parametrize('test_input,expected', [
    ('level', True),
    ('python', False),
    ('racecar', True),
    ('', True)
])

def test_is_palindrom(test_input, expected):
    assert is_palindrom(test_input) == expected



import pytest
from main_dz import count_vowels


@pytest.mark.parametrize('test_input,expected', [
    ('аааААА', 6),
    ('прнгкТЛШ', 0),
    ('ОЛГРДнисмщд', 2),
    ('', 0)
])
def test_count_vowels(test_input, expected):
    assert count_vowels(test_input) == expected

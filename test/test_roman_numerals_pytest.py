from app.roman_numerals import pytest_parser
from pytest import mark

@mark.parametrize("s,expected", [("IX", 9), ("X", 10)])
def test_roman_numeral_parser(s, expected):
    result = pytest_parser(s)
    assert result == expected

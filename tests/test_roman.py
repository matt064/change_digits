from roman.roman import convert_digit
import pytest


def test_import_from_roman():
    try:
        from roman.roman import convert_digit
        assert callable(convert_digit), "convert_digit is not callable"
    except ImportError as error:
        assert False, error


def test_simple_roman_to_integer_number():
    wynik = convert_digit("LVI")    
    assert wynik == 56


def test_complex_roman_to_integer_number():
    wynik = convert_digit('MCMXCIII')
    assert wynik == 1993
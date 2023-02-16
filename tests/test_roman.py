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


def test_final_number_is_integer():
    wynik = convert_digit("VII")
    assert type(wynik) == int


def test_lowercase_roman_to_integer():
    wynik = convert_digit('cvii')
    assert wynik == 107


def test_one_letter_in_roman_is_wrong():
    with pytest.raises(ValueError):
        convert_digit("VIIr")


def test_wrong_string():
    with pytest.raises(ValueError):
        convert_digit("RT")


def test_integer_to_roman_number():
    wynik = convert_digit(1249)
    assert wynik == 'MCCXLIX'
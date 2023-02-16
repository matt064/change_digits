from roman.roman import convert_digit


def test_import_from_roman():
    try:
        from roman.roman import convert_digit
        assert callable(convert_digit), "convert_digit is not callable"
    except ImportError as error:
        assert False, error


def test_variable_is_none():
    assert convert_digit(" ") is None
    
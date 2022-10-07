from odyssey.version import example, Version


def test_example() -> None:
    expected = "Hello, World!"

    result = example()

    assert expected == result


def test_Version_eq_Version() -> None:
    expected = Version("1.0.0")

    result = Version()

    assert expected == result


def test_Version_eq_str() -> None:
    value = "1.0.0"

    result = Version()

    # Uses str __eq__
    assert not value == result

    # Uses Version __eq__
    assert not result == value

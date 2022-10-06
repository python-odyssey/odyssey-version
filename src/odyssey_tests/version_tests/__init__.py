from odyssey import version


def test_example():
    expected = "Hello, World!"

    result = version.example()

    assert expected == result

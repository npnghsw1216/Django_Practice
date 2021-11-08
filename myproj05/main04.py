from main04 import make_powered_list


def test_make_powered_list():
    numbers = [0, 1, 2, 3, 4]
    expected = [0, 1, 4, 9, 16]
    assert make_powered_list(numbers) == expected

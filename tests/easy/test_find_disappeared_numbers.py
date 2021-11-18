from leetcode_py.easy.find_disappeared_numbers import (
    find_disappeared_numbers,
    find_disappeared_numbers_bitflag,
)


def test_find_disappeared_numbers():
    assert find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert find_disappeared_numbers([1, 1]) == [2]


def test_find_disappeared_numbers_bitflag():
    assert find_disappeared_numbers_bitflag([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert find_disappeared_numbers_bitflag([1, 1]) == [2]

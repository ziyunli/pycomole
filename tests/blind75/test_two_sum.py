from leetcode.blind75.two_sum import two_sum


def test_two_sum() -> None:
    assert two_sum([], 0) == []
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 2, 3], 10) == []

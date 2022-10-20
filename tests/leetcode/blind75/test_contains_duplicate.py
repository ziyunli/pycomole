from leetcode.blind75.contains_duplicate import contains_duplicate


def test_contains_duplicate() -> None:
    assert contains_duplicate([1, 2, 3, 1])
    assert not contains_duplicate([1, 2, 3, 4])
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])

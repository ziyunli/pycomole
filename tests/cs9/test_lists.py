from cs9.lists import dedup, keep_nth_occurrences, two_sum


def test_dedup() -> None:
    assert dedup(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]
    assert dedup(["foo", "bar", "baz", "foo", "bar"]) == ["foo", "bar", "baz"]


def test_keep_nth_occurrences() -> None:
    assert keep_nth_occurrences(["a", "b", "a", "c", "b"], 0) == []
    assert keep_nth_occurrences(["a", "b", "a", "c", "b"], 1) == [
        "a",
        "b",
        "c",
    ]
    assert keep_nth_occurrences(["foo", "bar", "baz", "foo", "bar"], 2) == [
        "foo",
        "bar",
        "baz",
        "foo",
        "bar",
    ]


def test_two_sum() -> None:
    assert two_sum([2, 7, 11, 15], 8) == []
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]

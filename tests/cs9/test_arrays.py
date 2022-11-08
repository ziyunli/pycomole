from cs9.arrays import dedup, keep_nth_occurrences


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

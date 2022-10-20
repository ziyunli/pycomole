from collections import defaultdict
from typing import Dict, List


def dedup(lst: List[str]) -> List[str]:
    """
    Returns a copy of the input list with duplicates removed. \
        Preserve order in the original list as much as possible \
            (keep first occurrence).

    Examples:
        >>> dedup(["a", "b", "a", "c", "b"])
        ['a', 'b', 'c']
        >>> dedup(["foo", "bar", "baz", "foo", "bar"])
        ['foo', 'bar', 'baz']

    Args:
        lst: The input list to deduplicate

    Returns:
        a copy of the input list with duplicates removed
    """
    found = set()
    results = []
    for w in lst:
        if w not in found:
            results.append(w)
            found.add(w)
    return results


def keep_nth_occurrences(lst: List[str], n: int) -> List[str]:
    """
    Returns a copy of the input list that keeps nth occurrence. \
        Preserve order in the original list as much as possible. \

    Examples:
        >>> keep_nth_occurrences(["a", "b", "a", "c", "b"], 1)
        ['a', 'b', 'c']
        >>> keep_nth_occurrences(["foo", "bar", "baz", "foo", "bar"], 2)
        ["foo", "bar", "baz", "foo", "bar"]

    Args:
        lst: The input list to deduplicate
        n: The nth occurrence to keep

    Returns:
        a copy of the input list that keeps nth occurrence.
    """
    if n < 1:
        return []

    if n == 1:
        return dedup(lst)

    found: Dict[str, int] = defaultdict(int)
    results = []
    for w in lst:
        if w not in found or found[w] < n:
            found[w] += 1
            results.append(w)
    return results

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

    Notes:
        - The perfect use case for a set.
        - If Set is not available, use a dictionary/hash map.
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

    Notes:
        - Think about where a string has fewer than n occurrences. \
            Note we keep it in the result, but alternative you can \
                only include nth occurrence if it exists.
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


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given a list of numbers and a target number, return the indices \
        of the two numbers that add up to the target.

    Examples:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
        >>> two_sum([3, 2, 4], 6)
        [1, 2]
        >>> two_sum([3, 3], 6)
        [0, 1]

    Args:
        nums: The list of numbers
        target: The target number

    Returns:
        The indices of the two numbers that add up to the target

    Notes:
        - Use a dictionary to keep track of the number and its index
    """
    found: Dict[int, int] = {}
    for i, n in enumerate(nums):
        if target - n in found:
            return [found[target - n], i]
        found[n] = i

    return []

from collections import defaultdict
from typing import Dict, Set


def reverse_words(s: str) -> str:
    """
    Reverses the order of the letters in each word from the input
    while preserving the word order and spacing.

    Examples:
        >>> reverse_words("moo cow bark dog")
        oom woc krab god

    Args:
        s: An input string

    Returns:
        A string that reverses the order of the letters in each word \
            from the input while preserving the word order and spacing

    Notes:
        - Clarify how many spaces/tabs/newlines are between words
        - A naive approach is to split the string into words using split() \
        and reverse the words using reverse() and then join the words
        - A more efficient approach is to use a stack in a single pass
    """
    results = []
    stack = []
    for c in s:
        # Assume the string only has alphabet and numeric characters
        if c.isalnum():
            stack.append(c)
        else:
            while stack:
                results.append(stack.pop())
            results.append(c)  # preserve the same number of spaces

    while stack:
        results.append(stack.pop())
    return "".join(results)


def has_balanced_parentheses(s: str) -> bool:
    """
    Checks if a string has balanced parentheses

    Examples:
        >>> has_balanced_parentheses("()")
        True
        >>> has_balanced_parentheses("(()")
        False
        >>> has_balanced_parentheses("(test)")
        True

    Args:
        s: The input string to check for balanced parentheses

    Returns:
        a boolean indicating whether the given string has balanced \
            parentheses

    Notes:
        - A good place to use stack to keep track of open parentheses
        - Note that the input string can have other characters
    """
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            stack.pop()
    return not stack


def has_balanced_brackets(s: str) -> bool:
    """
    Checks if a string has balanced brackets "()", "[]" or "{}".

    Examples:
        >>> has_balanced_brackets("()[]{}")
        True
        >>> has_balanced_brackets("(")
        False
        >>> has_balanced_brackets("([)]")
        False

    Args:
        s: The input string to check for balanced brackets

    Returns:
        a boolean indicating whether the given string has balanced \
            brackets

    Notes:
        - A good place to use stack to keep track of open brackets
        - Note that the input string can have other characters
        - Use hash to map opening brackets to closing brackets
    """
    stack = []
    matching_pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    for c in s:
        if c in ["(", "[", "{"]:
            stack.append(c)
        elif c in [")", "]", "}"]:
            if not stack:
                return False
            if matching_pairs[stack.pop()] != c:
                return False
    return not stack


def longest_contiguous_substring(s: str) -> str:
    """
    Return the longest contiguous substring of 2 distinct characters \
        from an input string.

    Examples:
        >>> longest_contiguous_substring("abbaacab")
        abbaa
        >>> longest_contiguous_substring("abcefabbabaabefghghfa")
        abbabaab
        >>> longest_contiguous_substring("aabceddddcdccecabceftg")
        ddddcdcc
        >>> longest_contiguous_substring("acbabbcbca")
        bbcbc

    Args:
        s: The input string

    Returns:
        The longest contiguous substring of 2 distinct characters \
            from the input string

    Notes:
        - Use a dictionary to keep the latest 2 distinct characters \
            and when they first show up
        - Use a sliding window to keep track of the longest substring
    """
    if len(s) < 2:
        return ""

    if len(s) == 2:
        if len(set(s)) == 2:
            return s
        else:
            return ""

    longest = ""
    start = 0  # sliding window is [start, i)
    chars: Set[str] = set()
    for i, c in enumerate(s):
        if len(chars) < 2:
            chars.add(c)
        else:  # len(chars) == 2
            if c not in chars:
                # See if we have a new longest substring
                if i - start > len(longest):
                    longest = s[start:i]
                # Find the new starting index of the sliding window
                start = i - 1
                while start > 0:
                    if s[start - 1] != s[start]:
                        break
                    start -= 1
                # Remote the other character
                chars.remove(s[start - 1])
                # Add the new character
                chars.add(c)
    return longest


def abbrev(s: str) -> str:
    """
    Returns an abbreviation form \
        `<first letter> <number of omitted letters> <last letter>` \
            of the input string.

    Examples:
        >>> abbrev("internationalization")
        i18n
        >>> abbrev("localization")
        l10n

    Args:
        s: the input string

    Returns:
        An abbreviation of the input string in the form of \
            `<first letter> <number of omitted letters> <last letter>.`

    Notes:
        - Handle edge cases where the input string is too short \
            e.g. 0-, 1-, 2-, 3-letter strings)
        - Clarify if the input has non-alphabet letters
    """
    if len(s) <= 3:
        return s  # Nothing to abbrev

    head = s[0]
    tail = s[-1]
    return "".join([head, str(len(s) - 2), tail])


def anagram(s: str, t: str) -> bool:
    """
    Checks if the given two strings to be anagram of each other.
    Two strings are said to be anagrams of one another if you can turn \
        the first string into the second by rearranging its letters.

    Examples:
        >>> anagram("table", "bleat")
        True
        >>> anagram("foo", "bar")
        False

    Args:
        s: The first string
        t: The second string

    Returns:
        A boolean indicating whether the given two strings are anagrams \
            of each other

    Notes:
        - Anagrams always have the same length
        - Use a dictionary to keep track of the letter counts (histogram)
    """
    if len(s) != len(t):
        return False

    histogram_s: Dict[str, int] = defaultdict(int)
    for ch in s.lower():
        histogram_s[ch] += 1

    histogram_t: Dict[str, int] = defaultdict(int)
    for ch in t.lower():
        histogram_t[ch] += 1

    return histogram_s == histogram_t

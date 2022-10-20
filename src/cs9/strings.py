from collections import deque
from typing import Deque, Dict


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
    longest = None
    chars: Deque[str] = deque()  # the latest 2 distinct characters
    idx: Dict[str, int] = {}  # idx of the 2 characters
    for i, c in enumerate(s):
        if len(idx) < 2:
            chars.append(c)
            idx[c] = i
        else:  # At most 2 distinct characters
            if c not in idx:
                # Calculate the length of the current 2-letter substring
                head = chars[0]
                span = (idx[head], i)
                # Update the longest substring if it's longer
                if (
                    longest is None
                    or span[1] - span[0] > longest[1] - longest[0]
                ):
                    longest = span
                # Note the head might not be the one to remove
                # e.g. bbbaaabbbc, we keep b and need to move its idx
                prev = s[i - 1]
                # Find the new idx for prev
                new_head = i - 1
                while new_head > 0:
                    if s[new_head - 1] != s[new_head]:
                        break
                    new_head -= 1
                idx[prev] = new_head
                idx[c] = i
                # Remove the other chacter
                del idx[s[new_head - 1]]
                # The new 2-letter set
                chars = deque([prev, c])
            # otherwise, keep going
    return "" if longest is None else s[longest[0] : longest[1]]

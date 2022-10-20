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
    """

    def with_stack(s: str) -> str:
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

    def naive(s: str) -> str:
        words = s.split()
        reverse_words = []
        for w in words:
            reverse_words.append(w[::-1])
        return " ".join(reverse_words)

    return with_stack(s)


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

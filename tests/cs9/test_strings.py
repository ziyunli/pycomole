from cs9.strings import (
    abbrev,
    has_balanced_brackets,
    has_balanced_parentheses,
    longest_contiguous_substring,
    reverse_words,
)


def test_has_balanced_parentheses() -> None:
    assert has_balanced_parentheses("()")
    assert has_balanced_parentheses("()()")
    assert has_balanced_parentheses("((()))")
    assert has_balanced_parentheses("(()())")

    assert not has_balanced_parentheses("(")
    assert not has_balanced_parentheses(")")
    assert not has_balanced_parentheses("))")
    assert not has_balanced_parentheses("(()")


def test_has_balanced_brackets() -> None:
    assert has_balanced_brackets("()")
    assert has_balanced_brackets("[]")
    assert has_balanced_brackets(r"{}")
    assert has_balanced_brackets("()()")
    assert has_balanced_brackets("[]()")
    assert has_balanced_brackets(r"{}()")
    assert has_balanced_brackets("()[]")
    assert has_balanced_brackets("[][]")
    assert has_balanced_brackets(r"{}{}")
    assert has_balanced_brackets("()[]{}")
    assert has_balanced_brackets("[](){}")
    assert has_balanced_brackets(r"{}()[]")
    assert has_balanced_brackets("((()))")
    assert has_balanced_brackets("[[[]]]")
    assert has_balanced_brackets(r"{{{{{}}}}}")
    assert has_balanced_brackets("((()))[]{}")
    assert has_balanced_brackets("[[[]]](){}")
    assert has_balanced_brackets(r"{{{{{}}}}}()[]")
    assert has_balanced_brackets(r"(((hello)))[world]{!}")

    assert not has_balanced_brackets("(")
    assert not has_balanced_brackets("[")
    assert not has_balanced_brackets(r"{")
    assert not has_balanced_brackets(")")
    assert not has_balanced_brackets("]")
    assert not has_balanced_brackets(r"}")
    assert not has_balanced_brackets("((")
    assert not has_balanced_brackets("[[")
    assert not has_balanced_brackets(r"{{")
    assert not has_balanced_brackets("))")
    assert not has_balanced_brackets("]]")
    assert not has_balanced_brackets(r"}}")
    assert not has_balanced_brackets("(()")
    assert not has_balanced_brackets("[[]")
    assert not has_balanced_brackets(r"{{}")
    assert not has_balanced_brackets("())")
    assert not has_balanced_brackets("][")
    assert not has_balanced_brackets(r"}{")
    assert not has_balanced_brackets("([)]")
    assert not has_balanced_brackets(r"((()))[]{}(")


def test_reverse_words() -> None:
    assert reverse_words("moo cow bark dog") == "oom woc krab god"
    assert (
        reverse_words("moo cow  bark   dog    ") == "oom woc  krab   god    "
    )


def test_longest_contiguous_substring() -> None:
    assert longest_contiguous_substring("") == ""
    assert longest_contiguous_substring("a") == ""
    assert longest_contiguous_substring("aa") == ""
    assert longest_contiguous_substring("ab") == "ab"
    assert longest_contiguous_substring("abbaacab") == "abbaa"
    assert longest_contiguous_substring("abcefabbabaabefghghfa") == "abbabaab"
    assert longest_contiguous_substring("aabceddddcdccecabceftg") == "ddddcdcc"
    assert longest_contiguous_substring("acbabbcbca") == "bbcbc"


def test_abbrev() -> None:
    assert abbrev("") == ""
    assert abbrev("a") == "a"
    assert abbrev("ab") == "ab"
    assert abbrev("abc") == "abc"
    assert abbrev("localization") == "l10n"
    assert abbrev("internationalization") == "i18n"

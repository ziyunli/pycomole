from cs9.strings import has_balanced_brackets, has_balanced_parentheses


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
    assert not has_balanced_brackets(r"((()))[]{}(")
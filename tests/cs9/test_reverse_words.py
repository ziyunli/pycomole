from cs9.strings import reverse_words


def test_reverse_words() -> None:
    assert reverse_words("moo cow bark dog") == "oom woc krab god"
    assert (
        reverse_words("moo cow  bark   dog    ") == "oom woc  krab   god    "
    )

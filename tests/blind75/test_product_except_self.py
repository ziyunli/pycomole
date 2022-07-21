from leetcode.blind75.product_except_self import product_except_self


def test_product_except_self() -> None:
    assert product_except_self([]) == []
    assert product_except_self([1]) == [0]
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

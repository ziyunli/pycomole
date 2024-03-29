from leetcode.blind75.best_time_to_buy_and_sell_stock import (
    max_profit,
    max_profit_brute_force,
)


def test_max_profit_brute_force() -> None:
    assert max_profit_brute_force([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit_brute_force([7, 6, 4, 3, 1]) == 0
    assert max_profit_brute_force([7]) == 0


def test_max_profit() -> None:
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([7]) == 0

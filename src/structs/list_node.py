from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, nxt: Optional["ListNode"] = None):
        self.val = val
        self.next = nxt

from typing import List

"""
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not
appear in nums.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:

Input: nums = [1,1]
Output: [2]



Constraints:

    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n



Follow up: Could you do it without extra space and in O(n) runtime? You
may assume the returned list does not count as extra space.
"""


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    n = len(nums)
    ns = set(range(1, n + 1))

    for v in nums:
        if v in ns:
            ns.remove(v)
    return list(ns)


def find_disappeared_numbers_bitflag(nums: List[int]) -> List[int]:
    n = len(nums)
    flags = 0
    ret = []
    for v in nums:
        flags = flags | (1 << (v - 1))

    for i in range(0, n):
        b = (flags >> i) & 1
        if not b:
            ret.append(i + 1)

    return ret

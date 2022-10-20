"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    hit = set()
    for _, n in enumerate(nums):
        if n in hit:
            return True
        else:
            hit.add(n)

    return False
"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a
32-bit integer.

You must write an algorithm that runs in O(n) time and without using the
 division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a
32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity
analysis.)
"""

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)

    left_products = []
    prev_product = 1
    for i in range(n):
        left_products.append(prev_product)
        prev_product = prev_product * nums[i]

    right_products = []
    prev_product = 1
    for j in range(n):
        right_products.append(prev_product)
        prev_product = prev_product * nums[n - 1 - j]

    for i in range(n):
        nums[i] = left_products[i] * right_products[n - 1 - i]
    return nums


def product_except_self_mem_optimal(nums: List[int]) -> List[int]:
    ans = [1 for _ in nums]

    lproduct = 1
    rproduct = 1
    for i in range(len(nums)):
        ans[i] = ans[i] * lproduct
        ans[-1 - i] = ans[-1 - i] * rproduct
        lproduct = lproduct * nums[i]
        rproduct = rproduct * nums[-1 - i]

    return ans

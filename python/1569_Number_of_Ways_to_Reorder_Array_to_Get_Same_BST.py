from math import comb


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def recursive(nums: List[int]):
            if len(nums) <= 2:
                return 1
            left = [value for value in nums if value < nums[0]]
            right = [value for value in nums if value > nums[0]]
            return comb(len(left) + len(right), len(right)) * recursive(left) * recursive(right)
        return (recursive(nums) - 1) % (10 ** 9 + 7)

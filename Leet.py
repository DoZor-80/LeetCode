class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Find indices of the terms.

        Given an array of integers nums and an integer target, return indices
        of the two numbers such that they add up to target.
        """
        result = []
        i = 0
        while i < len(nums):    # Let's try something faster
            try:
                j = nums.index(target - nums[i], i + 1)
                result += [i, j]
                break
            except ValueError:
                i += 1

        return result

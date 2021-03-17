class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Find indices of the terms.

        Given an array of integers nums and an integer target, return indices
        of the two numbers such that they add up to target.
        """
        my_dict = {}
        result = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_dict.keys():
                result = [my_dict[complement], i]
                break
            my_dict[nums[i]] = i

        return result

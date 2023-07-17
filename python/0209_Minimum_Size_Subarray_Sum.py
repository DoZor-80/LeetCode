class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        left = 0
        current = 0
        for i in range(len(nums)):
            current += nums[i]
            while current >= target:
                window_size = i - left + 1
                if window_size < result:
                    result = window_size
                current -= nums[left]
                left += 1
        return 0 if result == float('inf') else result

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        result = []
        current_sum = None
        d = 2 * k + 1
        for i in range(len(nums)):
            if i - k >= 0 and i + k < len(nums):
                if current_sum is None:
                    current_sum = sum(nums[i-k:i+k+1])
                else:
                    current_sum = current_sum - nums[i-k-1] + nums[i+k]
                result.append(floor(current_sum / d))
            else:
                result.append(-1)
        return result

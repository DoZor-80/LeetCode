class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = {}

        def recursive_diff(i, j):
            if dp.get((i, j)):
                return dp[i, j]
            if i == j:
                return nums[i]
            left = nums[i] - recursive_diff(i + 1, j)
            right = nums[j] - recursive_diff(i, j - 1)

            dp[i, j] = max(left, right)
            return dp[i, j]

        return recursive_diff(0, len(nums) - 1) >= 0

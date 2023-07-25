class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        result = 0
        for i in range(len(arr)):
            subsequence = dp.get(arr[i] - difference, 0)
            dp[arr[i]] = subsequence + 1
            if result < dp[arr[i]]:
                result = dp[arr[i]]
        return result

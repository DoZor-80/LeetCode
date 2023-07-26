class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        def binary_search(arr, value):
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if value < arr[mid]:
                    right = mid
                else:
                    left = mid + 1
            return left

        events = sorted(events)
        n = len(events)
        start_days = [event[0] for event in events]

        dp = {i: [0] * (n + 1) for i in range(k + 1)}

        for day in range(n - 1, -1, -1):
            next_day = binary_search(start_days, events[day][1])
            for count in range(1, k + 1):
                dp[count][day] = max(dp[count][day + 1], events[day][2] + dp[count - 1][next_day])

        return dp[k][0]

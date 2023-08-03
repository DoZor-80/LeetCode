class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        result = 0
        left = float('-inf')
        for interval in sorted_intervals:
            if interval[0] >= left:
                left = interval[1]
            else:
                result += 1
        return result

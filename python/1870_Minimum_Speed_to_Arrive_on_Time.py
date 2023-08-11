class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def required_time(dist, speed):
            time = 0
            for i in range(len(dist)):
                t = dist[i] / speed
                time += t if i == (len(dist) - 1) else ceil(t)
            return time

        left = 1
        right = 10_000_000
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if required_time(dist, mid) <= hour:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result

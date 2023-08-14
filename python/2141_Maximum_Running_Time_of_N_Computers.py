class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries = sorted(batteries)
        extra = sum(batteries[:-n])
        in_use = batteries[-n:]

        for i in range(n - 1):
            if extra // (i + 1) < in_use[i + 1] - in_use[i]:
                return in_use[i] + extra // (i + 1)
            extra -= (i + 1) * (in_use[i + 1] - in_use[i])

        return in_use[-1] + extra // n

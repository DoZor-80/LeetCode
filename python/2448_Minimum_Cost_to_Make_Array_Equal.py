class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nums, cost = zip(*sorted(zip(nums, cost)))
        d = {}
        for _num, _cost in zip(nums, cost):
            if _num not in d:
                d[_num] = _cost
            else:
                d[_num] += _cost
        nums, cost = list(d.keys()), list(d.values())
        min_cost = current_cost = sum([abs(nums[0] - nums[i]) * cost[i] for i in range(len(nums))])
        multiplier_1 = 0
        multiplier_2 = sum(cost)

        for i in range(1, len(nums)):
            step = nums[i] - nums[i-1]
            multiplier_1 = multiplier_1 + cost[i-1]
            multiplier_2 = multiplier_2 - cost[i-1]
            current_cost = current_cost + step * (multiplier_1 - multiplier_2)
            if current_cost < min_cost:
                min_cost = current_cost
        return min_cost

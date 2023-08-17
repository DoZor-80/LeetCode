class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = [[nums[0]]]

        for i in range(1, n):
            r = []
            for permutation in result:
                for j in range(i + 1):
                    p = permutation.copy()
                    p.insert(j, nums[i])
                    r.append(p)
            result = r
        return result

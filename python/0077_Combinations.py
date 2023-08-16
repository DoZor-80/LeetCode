class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def add_number(c: list, index: int, r: list):
            if len(c) >= k:
                r.append(c.copy())
                return
            if index > n:
                return
            add_number(c, index + 1, r)
            c.append(index)
            add_number(c, index + 1, r)
            c.pop(-1)

        result = []
        combination = []
        add_number(combination, 1, result)
        return result

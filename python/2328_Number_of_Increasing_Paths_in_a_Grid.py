class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # Define the size n x m
        n = len(grid)
        m = len(grid[0])
        dp = {}

        def recursive(_i: int, _j: int, current: int) -> int:
            if dp.get((_i, _j, current)) is not None:
                return dp[(_i, _j, current)]
            counter = 1
            # There are 4 directions for each matrix element
            if _i - 1 >= 0 and current < grid[_i - 1][_j]:
                counter += recursive(_i - 1, _j, grid[_i - 1][_j])
            if _i + 1 < n and current < grid[_i + 1][_j]:
                counter += recursive(_i + 1, _j, grid[_i + 1][_j])
            if _j - 1 >= 0 and current < grid[_i][_j - 1]:
                counter += recursive(_i, _j - 1, grid[_i][_j - 1])
            if _j + 1 < m and current < grid[_i][_j + 1]:
                counter += recursive(_i, _j + 1, grid[_i][_j + 1])
            dp[(_i, _j, current)] = counter
            return counter
        
        result = 0
        for i in range(n):
            for j in range(m):
                result += recursive(i, j, grid[i][j])
        return result % (10 ** 9 + 7)
      

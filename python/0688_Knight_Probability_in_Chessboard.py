class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
        dp = {}

        def recursive_move(i, j, moves_left):
            if dp.get((i, j, moves_left)):
                return dp[i, j, moves_left]
            if not (0 <= i < n and 0 <= j < n):
                dp[i, j, moves_left] = 0
                return 0
            if moves_left == 0:
                dp[i, j, moves_left] = 1
                return 1
            s = 0
            for move in moves:
                new_i = i + move[0]
                new_j = j + move[1]
                s += recursive_move(new_i, new_j, moves_left - 1)
            s /= 8
            dp[i, j, moves_left] = s
            return s

        return recursive_move(row, column, k)

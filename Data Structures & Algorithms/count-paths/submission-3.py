class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dfs(m, n, 0, 0, {})

    def dfs(self, m, n, row, col, memo):
        key = (row, col)
        if key in memo:
            return memo[key]

        row_inbounds = row < m
        col_inbounds = col < n

        if not row_inbounds or not col_inbounds:
            return 0

        if row == m - 1 and col == n - 1:
            return 1

        deltas = [(1, 0), (0, 1)]
        count = 0
        for delta in deltas:
            row_moved, col_moved = delta
            count += self.dfs(m, n, row + row_moved, col + col_moved, memo) 
        memo[key] = count
        return memo[key] 


        
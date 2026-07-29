class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(row, col):
            if grid[row][col] != 1:
                return 0
            
            grid[row][col] = 0
            total = 0
            if row < len(grid) - 1:
                total += dfs(row + 1, col)
            if row > 0:
                total += dfs(row - 1, col)
            if col < len(grid[0]) - 1:
                total += dfs(row, col + 1)
            if col > 0:
                total += dfs(row, col - 1)
            return (total + 1)
        
        row = len(grid)
        col = len(grid[0])
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row, col):
            if grid[row][col] == "0":
                return False
            
            grid[row][col] = "0"
            if row < len(grid) - 1:
                dfs(row + 1, col)
            if row > 0:
                dfs(row - 1, col)
            if col < len(grid[0]) - 1:
                dfs(row, col + 1)
            if col > 0:
                dfs(row, col - 1)
            return True
        
        row = len(grid)
        col = len(grid[0])
        count = 0
        for r in range(row):
            for c in range(col):
                if dfs(r, c):
                    count += 1
        return count
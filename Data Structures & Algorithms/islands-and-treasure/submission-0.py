class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        row = len(grid)
        col = len(grid[0])
        INF = 2147483647

        que = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    que.append([r, c])

        while que:
            r, c = que.popleft()

            if r < len(grid) - 1 and grid[r + 1][c] == INF:
                que.append([r + 1, c])
                grid[r + 1][c] = grid[r][c] + 1
            if r > 0 and grid[r - 1][c] == INF:
                que.append([r - 1, c])
                grid[r - 1][c] = grid[r][c] + 1
            if c < len(grid[0]) - 1 and grid[r][c + 1] == INF:
                que.append([r, c + 1])
                grid[r][c + 1] = grid[r][c] + 1
            if c > 0 and grid[r][c - 1] == INF:
                que.append([r, c - 1])
                grid[r][c - 1] = grid[r][c] + 1
        
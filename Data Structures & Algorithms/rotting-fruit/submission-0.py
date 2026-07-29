class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        que = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    que.append([r, c])
                    grid[r][c] = 0
        
        while que:
            r, c = que.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < row and nr >= 0 and nc < col and nc >= 0 and grid[nr][nc] == 1:
                    que.append([nr, nc])
                    grid[nr][nc] = grid[r][c] - 1
        
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return -1
                res = min(res, grid[r][c])
        return -res
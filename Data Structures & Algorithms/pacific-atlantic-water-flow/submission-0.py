class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(row, col, visit):
            visit.add((row, col))

            for r, c in direction:
                next_row = row + r
                next_col = col + c

                if (
                    0 <= next_row < len(heights) and
                    0 <= next_col < len(heights[0]) and
                    heights[row][col] <= heights[next_row][next_col] and
                    (next_row, next_col) not in visit
                ):
                    dfs(next_row, next_col, visit)
        
        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, atlantic)
        
        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atlantic)
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        
        return res
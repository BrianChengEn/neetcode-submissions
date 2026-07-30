class Solution:
    def solve(self, board: List[List[str]]) -> None:
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visit = set()
        def dfs(row, col):
            if board[row][col] == "X":
                return
            visit.add((row, col))

            for r, c in direction:
                next_row = row + r
                next_col = col + c
                if(
                    0 <= next_row < len(board) and 
                    0 <= next_col < len(board[0]) and
                    (next_row, next_col) not in visit and
                    board[next_row][next_col] == "O"
                ):
                    dfs(next_row, next_col)

        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)
        
        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row, col) not in visit:
                    board[row][col] = "X"
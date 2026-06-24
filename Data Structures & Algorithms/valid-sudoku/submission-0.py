class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count1 = [0] * 9
        count2 = [0] * 9
        count3 = [0] * 9

        for i in range(9):
            count1 = [0] * 9
            count2 = [0] * 9
            for j in range(9):
                if board[i][j] != ".":
                    if count1[int(board[i][j]) - 1]:
                        return False
                    else:
                        count1[int(board[i][j]) - 1] = 1
                if board[j][i] != ".":
                    if count2[int(board[j][i]) - 1]:
                        return False
                    else:
                        count2[int(board[j][i]) - 1] = 1

        for i in range(3):
            for j in range(3):
                count3 = [0] * 9
                for k in range(3):
                    for l in range(3):
                        if board[i * 3 + k][j * 3 + l] == ".":
                            continue
                        if count3[int(board[i * 3 + k][j * 3 + l]) - 1]:
                            return False
                        else:
                            count3[int(board[i * 3 + k][j * 3 + l]) - 1] = 1
        
        return True
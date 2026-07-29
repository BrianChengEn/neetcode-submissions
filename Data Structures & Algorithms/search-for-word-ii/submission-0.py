class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        root = TrieNode()

        for word in words:
            cur = root
            for w in word:
                if w not in cur.children:
                    cur.children[w] = TrieNode()
                cur = cur.children[w]
            cur.word = word
        
        def dfs(row, col, node):
            char = board[row][col]

            if char not in node.children:
                return
            
            next_node = node.children[char]
            if next_node.word is not None:
                res.append(next_node.word)
                next_node.word = None
            
            board[row][col] = "#"
            if row < len(board) - 1:
                dfs(row + 1, col, next_node)
            if row > 0:
                dfs(row - 1, col, next_node)
            if col < len(board[0]) - 1:
                dfs(row, col + 1, next_node)
            if col > 0:
                dfs(row, col - 1, next_node)
            board[row][col] = char
        
        row = len(board)
        col = len(board[0])
        for r in range(row):
            for c in range(col):
                dfs(r, c, root)
        return res
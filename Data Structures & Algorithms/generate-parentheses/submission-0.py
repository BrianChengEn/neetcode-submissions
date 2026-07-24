class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(openN, closeN):
            if openN == closeN == n:
                res.append("".join(path))
                return
            
            if openN < n:
                path.append("(")
                dfs(openN + 1, closeN)
                path.pop()
            
            if closeN < openN:
                path.append(")")
                dfs(openN, closeN + 1)
                path.pop()
        
        dfs(0, 0)
        return res
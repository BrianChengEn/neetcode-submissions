class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        path = []
        digitMap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def dfs(start):
            if path and len(path) == len(digits):
                res.append("".join(path.copy()))
                return
            
            for s in digitMap[digits[start]]:
                path.append(s)
                dfs(start + 1)
                path.pop()
        
        dfs(0)
        return res

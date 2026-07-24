class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(start, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    return
                cur.append(candidates[i])
                dfs(i + 1, cur, total + candidates[i])
                cur.pop()
        
        dfs(0, [], 0)
        return res
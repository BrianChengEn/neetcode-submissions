class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            for i in range(start, len(nums)):
                if total + nums[i] > target:
                    return
                cur.append(nums[i])
                dfs(i, cur, total + nums[i])
                cur.pop()
        
        dfs(0, [], 0)
        return res
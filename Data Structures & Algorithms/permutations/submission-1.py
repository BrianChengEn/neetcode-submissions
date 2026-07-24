class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def dfs(cur, seen):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                cur.append(nums[i])
                seen.add(nums[i])
                dfs(cur, seen)
                cur.pop()
                seen.remove(nums[i])

        dfs([], seen)
        return res
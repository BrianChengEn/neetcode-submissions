class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = sum(nums)

        if n % 2 == 1:
            return False
        
        target = n // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, -1, -1):
                if i >= num and dp[i - num]:
                    dp[i] = True

        return dp[target]
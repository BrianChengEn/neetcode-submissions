class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        
        def helper(left, right):
            first = 0
            second = 0

            for i in range(left, right):
                dp[i] = max(first + nums[i], second)
                first = second
                second = dp[i]
            
            return dp[right - 1]
        
        return max(helper(0, len(nums) - 1), helper(1, len(nums)))
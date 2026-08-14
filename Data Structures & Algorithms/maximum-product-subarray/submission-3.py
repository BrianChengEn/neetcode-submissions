class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_pro = [0] * n
        min_pro = [0] * n

        max_pro[0] = nums[0]
        min_pro[0] = nums[0]
        
        res = nums[0]

        for i in range(1, n):
            max_pro[i] = max(max_pro[i - 1] * nums[i], min_pro[i - 1] * nums[i], nums[i])
            min_pro[i] = min(max_pro[i - 1] * nums[i], min_pro[i - 1] * nums[i], nums[i])
            res = max(res, max_pro[i])

        return res
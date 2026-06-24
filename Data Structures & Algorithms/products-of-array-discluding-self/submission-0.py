class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        prod = 1
        zero_count = 0

        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                prod *= n
        
        for i in range(len(nums)):
            if zero_count > 1:
                res[i] = 0
            elif zero_count == 1:
                if nums[i] == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod // nums[i]
        
        return res
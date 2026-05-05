class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        count = {}
        for i in range(len(nums)):
            if target - nums[i] in count:
                return [count[target - nums[i]], i] 
            count[nums[i]] = i
        
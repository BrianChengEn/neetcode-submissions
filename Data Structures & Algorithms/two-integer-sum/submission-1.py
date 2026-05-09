class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k_num = {}
        for i in range(len(nums)):
            if target - nums[i] in k_num:
                return [k_num[target - nums[i]], i]
            k_num[nums[i]] = i
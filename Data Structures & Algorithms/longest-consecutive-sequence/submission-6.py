class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = set(nums)
        
        res = 0

        for n in mp:
            if n - 1 not in mp:
                length = 1
                while n + length in mp:
                    length += 1
                res = max(res, length)

        return res
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        lar = 0
        while l < r:
            water = (r - l) * min(heights[l], heights[r])
            if  water > lar:
                lar = water
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return lar
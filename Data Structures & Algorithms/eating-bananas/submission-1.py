class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_v = max(piles)
        l = 1
        r = max_v
        res = max_v
        while l <= r:
            k = (l + r) // 2
            h_cnt = 0
            for pile in piles:
                h_cnt += (pile + k - 1) // k
            if h_cnt <= h:
                r = k - 1
                res = k
            else:
                l = k + 1
        return res
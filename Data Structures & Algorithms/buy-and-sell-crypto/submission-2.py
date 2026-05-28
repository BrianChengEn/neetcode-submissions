class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        mini = prices[0]
        pro = 0
        for i in range(1, len(prices)):
            pro = max(pro, prices[i] - mini)
            mini = min(mini, prices[i])
        return pro
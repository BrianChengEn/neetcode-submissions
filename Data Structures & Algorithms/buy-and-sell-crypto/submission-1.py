class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        pro = 0
        for i in range(1, len(prices)):
            pro = max(pro, prices[i] - mini)
            mini = min(mini, prices[i])
        return pro
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        pro = 0
        for i in range(1, len(prices)):
            if prices[i] > mini:
                pro = max(pro, prices[i] - mini)
            else:
                mini = prices[i]
        return pro
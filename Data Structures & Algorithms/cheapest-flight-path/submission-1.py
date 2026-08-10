class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            temp = prices.copy()

            for source, destination, price in flights:
                if prices[source] == float("inf"):
                    continue
                
                temp[destination] = min(temp[destination], prices[source] + price)
            
            prices = temp
        
        return prices[dst] if prices[dst] != float("inf") else -1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        minBuy = prices[0]
        for sell in prices:
            p = max(p, sell - minBuy)
            if sell < minBuy:
                minBuy = sell
            
        return p
        

        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] < prices[r]:
                p = max(p, prices[r] - prices[l])
            else:
                l = r
            r = r + 1
            
        return p
        

        
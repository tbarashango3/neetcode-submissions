class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                curr = prices[j] - prices[i]
                if curr > p:
                    p = curr
        return p
        

        
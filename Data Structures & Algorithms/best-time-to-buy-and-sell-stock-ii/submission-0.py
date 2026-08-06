class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * (n)
        bought = False
        for i in range(0, n - 1):
            if prices[i] < prices[i + 1]:
                if not bought:
                    dp[i + 1] = dp[i] - prices[i]
                    bought = True
                else:
                    dp[i + 1] = dp[i]

            elif bought:
                dp[i + 1] = dp[i] + prices[i]
                bought = False
            else:
                dp[i + 1] = dp[i]
        print(dp)
        if bought:
            return max(max(dp), dp[-1] + prices[-1])
        return dp[-1]
        
        
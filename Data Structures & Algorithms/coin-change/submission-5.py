class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins = sorted(coins, reverse=True)
        #print(coins)
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            
            if amount in memo:
                return memo[amount]

            mincount = float('inf')
            for coin in coins:
                res = dfs(amount - coin)
                if res != -1:
                    mincount = min(mincount, res + 1)

            if mincount != float('inf'):
                memo[amount] = mincount
                return mincount
            memo[amount] = -1
            return -1

        return dfs(amount)
            

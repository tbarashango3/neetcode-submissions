class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prof = 0
        i = 0
        j = 1
        while i < j and j < n:
            print("Prices i: ", prices[i])
            print("Prices j: ", prices[j])
            if prices[i] < prices[j]:
                while j < n-1 and prices[j] < prices[j+1]:
                    j+=1
                prof += prices[j] - prices[i]
                i = j + 1
                j += 2
            else:
                i += 1
                j += 1
            print(prof)
        return prof
        



        
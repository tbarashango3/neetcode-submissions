class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l = 1
        r = max(piles)
        out = r
        while l <= r:
            k = (l + r) // 2
            tempH = 0
            for i in range(n):
                tempH += math.ceil(float(piles[i]) / k)
            if tempH > h:
                l = k + 1
            else:
                out = k
                r = k - 1
        return out
                    
        
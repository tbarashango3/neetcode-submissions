class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ans = False
        n = len(s1)
        m = len(s2)
        l = 0
        if m < n:
            return ans
        for r in range(m):
            
            while r - l + 1 > n:
                l += 1
            #print("s2: ",sorted(s2[l:r+1]))
            #print(sorted(s1))
            if sorted(s1) == sorted(s2[l:r+1]):
                return True
        return ans
            

        
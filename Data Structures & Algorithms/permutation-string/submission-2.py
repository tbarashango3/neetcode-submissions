class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        for i in range(n-m+1):
            temp = s2[i:i+m]
            print(temp)
            if sorted(temp) == sorted(s1):
                return True
        return False
        
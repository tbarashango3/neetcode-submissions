class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        for i in range(n-m+1):
            if s2[i] not in s1:
                continue
            temp = s2[i:i+m]
            if sorted(temp) == sorted(s1):
                return True
        return False
        
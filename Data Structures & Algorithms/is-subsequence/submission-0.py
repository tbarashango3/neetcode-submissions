class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        m = len(s)
        dp = [0] * (n + 1)
        i = 0
        j = 0
        while i < n and j < m:
            #print("t: ", t[i])
            #print("s", s[j])
            if t[i] == s[j]:
                dp[i] = dp[i-1] + 1
                j += 1
            else:
                dp[i] = dp[i-1]
            i += 1

        print(dp)
        return max(dp) == m


            
            

        
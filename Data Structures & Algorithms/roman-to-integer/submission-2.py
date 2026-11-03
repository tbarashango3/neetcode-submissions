class Solution:
    def romanToInt(self, s: str) -> int:
        m = {}
        m["I"] = 1
        m["V"] = 5
        m["X"] = 10
        m["L"] = 50
        m["C"] = 100
        m["D"] = 500
        m["M"] = 1000
        ans = 0
        n = len(s)
        i = n-1
        while i > -1:
            if i >= 1 and m[s[i]] > m[s[i-1]]:
                ans += m[s[i]] - m[s[i-1]]
                i-=2

            else:
                ans += m[s[i]]
                i-=1
        return ans
        
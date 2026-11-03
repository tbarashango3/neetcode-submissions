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
            if s[i] == "V" and s[i-1] == "I":
                ans += 4
                i-=2
            elif s[i] == "X" and s[i-1] == "I":
                ans += 9
                i-=2
            elif s[i] == "L" and s[i-1] == "X":
                ans += 40
                i-=2
            elif s[i] == "C" and s[i-1] == "X":
                ans += 90
                i-=2
            elif s[i] == "D" and s[i-1] == "C":
                ans += 400
                i-=2
            elif s[i] == "M" and s[i-1] == "C":
                ans += 900
                i-=2
            else:
                ans += m[s[i]]
                i-=1
        return ans



        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = {}
        n = len(s)
        maxf = 0
        ans = 0
        

        L = 0
        for R in range(n):
            m[s[R]] = 1 + m.get(s[R], 0)
            maxf = max(maxf, m[s[R]])
            while R - L + 1 - maxf > k:
                m[s[L]] -= 1
                L += 1
            ans = max(ans, R - L + 1)

        return ans
        
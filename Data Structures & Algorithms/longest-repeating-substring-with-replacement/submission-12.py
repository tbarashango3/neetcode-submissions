class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        n = len(s)
        for i in range(n):
            m = {}
            maxf = 0
            for j in range(i, n):
                m[s[j]] = m.get(s[j], 0) + 1
                maxf = max(maxf, m[s[j]])
                if j - i + 1 - maxf <= k:
                    length = max(length, j - i + 1)

        return length


        
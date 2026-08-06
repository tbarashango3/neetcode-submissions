class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        n = len(s)
        cs = set()
        for c in s:
            cs.add(c)
        for char in cs:
            l = 0
            count = 0
            for r in range(n):
                if s[r] == char:
                    count += 1
                while (r - l + 1) - count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1

                length = max(length, r - l + 1)

        return length


        
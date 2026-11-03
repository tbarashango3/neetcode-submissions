class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        cs = set()
        l = 0

        for i in range(n):
            while s[i] in cs:
                cs.remove(s[l])
                l += 1
            cs.add(s[i])
            ans = max(i - l + 1, ans)

        return ans
        
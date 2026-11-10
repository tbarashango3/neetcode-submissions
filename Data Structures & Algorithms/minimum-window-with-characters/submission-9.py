class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = s
        n = len(s)
        m = len(t)
        tmap = {}
        if m > n:
            return ""
        if m == n:
            if sorted(s) == sorted(t):
                return s
            else:
                return ""
        found = False
        have = 0
        for tl in t:
            tmap[tl] = 1 + tmap.get(tl, 0)
        need = len(tmap)
        L = 0
        smap = {}
        for R in range(n):
            smap[s[R]] = 1 + smap.get(s[R], 0)

            if s[R] in tmap and smap[s[R]] == tmap[s[R]]:
                have += 1

            while have == need:
                found = True

                if R - L + 1 < len(ans):
                    ans = s[L:R+1]

                if s[L] in smap:
                    smap[s[L]] -= 1

                if s[L] in tmap and smap[s[L]] < tmap[s[L]]:
                    have -= 1

                L += 1

        return ans if found else ""

            

        
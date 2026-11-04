class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        n = len(s)
        m = len(p)

        if len(p) > len(s):
            return ans

        pmap = {}
        for pl in p:
            pmap[pl] = 1 + pmap.get(pl, 0)
        
        L = 0
        smap = {}
        print(pmap)
        for R in range(n):
            smap[s[R]] = 1 + smap.get(s[R], 0)
            while(R - L + 1 > m):
                if smap[s[L]] == 1:
                    del smap[s[L]]
                else:
                    smap[s[L]] -= 1
                L += 1
            if pmap == smap:
                ans.append(L)
            print(smap)
        return ans
            


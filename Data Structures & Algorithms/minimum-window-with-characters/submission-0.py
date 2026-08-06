class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        short = list(s)
        tlist1 = list(t)
        for char in list(s):
            if char in tlist1:
                tlist1.remove(char)
        if len(tlist1) > 0:
            return ""

        for i in range(n):
            count = 0
            tlist = list(t)
            for j in range(i, n):
                r = s[j]
                if s[j] in tlist:
                    tlist.remove(s[j])
                    if len(tlist) == 0:
                        tempS = s[i:j+1]
                        if len(tempS) < len(short):
                            short = tempS
                        break
        return "".join(short)

        

        
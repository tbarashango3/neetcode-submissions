class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            sort = "".join(sorted(s))
            print(sort)
            if sort not in m:
                m[sort] = [s]
            else:
                m[sort].append(s)
        return list(m.values())

        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        m = {}

        for st in strs:
            ss = ''.join(sorted(st))
            if ss not in m:
                m[ss] = [st]
            else:
                m[ss].append(st)
        
        return list(m.values())

        
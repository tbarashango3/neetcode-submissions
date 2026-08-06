class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long = 1
        n = len(s)
        if n < 1:
            return 0
        for i in range(n):
            sum = 0
            m = set()
            for j in range(i, len(s)):
                print(j)
                if s[j] not in m:
                    m.add(s[j])
                    sum += 1
                    long = max(long, sum)
                else:
                    long = max(long, sum)
                    break
        return long


                
                


        
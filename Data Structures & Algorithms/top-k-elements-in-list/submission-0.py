class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d.keys():
                d[num] = 1
            else:
                d[num] += 1
        ans = sorted(d.items(), key=lambda x: x[1], reverse=True)
        fin = []
        for i in range(k):
            fin.append(ans[i][0])
        return fin
        
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1
        sortedmap = sorted(m.items(), key=lambda x: x[1], reverse=True)
        ans = []
        #print(sortedmap[0:k])
        for i in range(k):
            ans.append(sortedmap[i][0])
        return ans


        
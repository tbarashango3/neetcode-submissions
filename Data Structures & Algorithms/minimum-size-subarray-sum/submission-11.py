class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) >= target:
            n = len(nums)
            res = n
            for i in range(n):
                curr = 0
                for j in range(i, n):
                    curr += nums[j]
                    #print(curr)
                    if curr >= target:
                        res = min(res, j-i+1)
                        break
            return res


        return 0

        
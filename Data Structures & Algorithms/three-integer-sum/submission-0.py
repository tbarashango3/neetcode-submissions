class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        out = []
        for i in range(n-2):
            for j in range(1, n-1):
                for k in range(2, n):
                    if i == j or i == k or j == k:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        if sorted([nums[i], nums[j], nums[k]]) not in out:
                            out.append(sorted([nums[i], nums[j], nums[k]]))
        return out
        
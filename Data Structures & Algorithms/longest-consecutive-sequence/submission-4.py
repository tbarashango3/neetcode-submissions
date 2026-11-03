class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        s = set(nums)
        for ns in s:
            if ns - 1 not in s:
                streak = 1
                while(ns + streak in s):
                    streak += 1
                ans = max(ans, streak)


        return ans
        
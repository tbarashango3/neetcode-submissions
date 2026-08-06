class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i, n in enumerate(nums):
            if n not in d:
                d[n] = 1
                print(d)
            else:
                return True;
        return False;
        
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        less = []
        eq = []
        more = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                eq.append(num)
            else:
                more.append(num)
        return less + eq + more

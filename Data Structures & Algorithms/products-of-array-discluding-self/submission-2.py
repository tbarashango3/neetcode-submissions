class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = nums[0]
        n = len(nums)
        output = []
        zero = False
        zeroCount = 0
        for i in range(1, n):
            if nums[i] == 0:
                zero = True
                zeroCount += 1
            else:
                prod *= nums[i]
        for i in range(n):
            if zero:
                if nums[i] == 0 and zeroCount == 1:
                    output.append(prod)
                else:
                    output.append(0)
            else:
                output.append(prod // nums[i])
        return output
        
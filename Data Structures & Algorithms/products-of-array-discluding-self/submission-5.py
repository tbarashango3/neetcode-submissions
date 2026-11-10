class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        s = 1
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1
            s *= num
        if zeroes > 1:
            return output

        for i in range(n):
            if nums[i] == 0 and zeroes == 1:
                temp = 1
                for num in nums:
                    if num != 0:
                        temp *= num
                output[i] = temp
            else:
                output[i] = s // nums[i]

        return output



        
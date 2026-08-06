class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        area = 0
        prevMax = 0
        for i in range(n):
            postMax = 0
            for j in range(i+1, n):
                if height[j] > postMax:
                    postMax = height[j]

            if postMax > height[i] and prevMax > height[i] and 0 < i < n:
                area += min(prevMax, postMax) - height[i]
            if height[i] > prevMax:
                prevMax = height[i]
        print(area)
        return area
            

            


        
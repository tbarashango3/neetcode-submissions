class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        if numRows == 1:
            return ans
        ans.append([1, 1])
        if numRows == 2:
            return ans
        for i in range (2, numRows):
            temp = []
            for j in range(i-1):
                temp.append(ans[i-1][j] + ans[i-1][j+1])
            ans.append([1] + temp + [1])
        return ans


            
        
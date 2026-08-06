class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        while i < n:
            if target > matrix[i][-1]:
                i += 1
                continue
            else:
                for j in range(m):
                    if matrix[i][j] == target:
                        return True
                return False
        return False
        
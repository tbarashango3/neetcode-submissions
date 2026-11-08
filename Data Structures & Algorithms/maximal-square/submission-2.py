class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # loop through each index in the matrix
        # if index is a one
        # detect square size
        # keep track of maximum square size
        # look at right, look down, look diagonal to the right/down
        # check if neighbor == 1
        # if square is found, expand size of square to prev size + 1

        square = 0
        row = len(matrix)
        col = len(matrix[0])

        def dfs(r, c):
            valid = True
            length = 1
            #track length, and add 1 to length when square is found
            # track r + length row and c + length col
            while(valid):
                if r + length >= row or c + length >= col:
                    valid = False
                    break
                for i in range(c, c + length + 1):
                    if matrix[r + length][i] == "0":
                        # looking at 0,2 and 1, 2 and 3, 2
                        # looking at 2, 0 and 2, 1 and 2, 2
                        valid = False
                        break
                for j in range(r, r+ length + 1):
                    if matrix[j][c + length] == "0":
                        valid = False
                        break
                if not valid:
                    break
                length += 1
            return length

            

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    #length = 0
                    res = dfs(i, j)
                    square = max(square, res)
        
        return square ** 2
        
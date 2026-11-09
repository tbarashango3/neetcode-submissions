class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # if 3 or more candies of same type touch, remove them
        # if candies below are removed, move above candies downward

        row = len(board)
        col = len(board[0])

        # find function scans boards for candy to crush and stores positions
        # crush function sets all candies in crush set to 0
        # drop function checks each column and moves all non-zero candies down to fill gaps
        # repeat until find is empty

        def find():
            crushset = set()
            for r in range(1, row - 1):
                for c in range(col):
                    if board[r][c] == 0:
                        continue
                    if board[r][c] == board[r-1][c] == board[r + 1][c]:
                        crushset.add((r, c))
                        crushset.add((r-1, c))
                        crushset.add((r+1, c))

            for r in range(row):
                for c in range(1, col - 1):
                    if board[r][c] == 0:
                        continue
                    if board[r][c] == board[r][c-1] == board[r][c+1]:
                        crushset.add((r, c))
                        crushset.add((r, c-1))
                        crushset.add((r, c+1))
            return crushset
        
        def crush(crushset):
            for r, c in crushset:
                board[r][c] = 0
        
        def drop():
            for r in range(row - 2, -1, -1):
                for c in range(col):
                    #print(r, c)
                    if board[r][c] != 0 and board[r+1][c] == 0:
                        i = 1
                        # r at index 5, 0 at index 6, i = 1
                        # r + i = 6
                        while (r + i + 1 < row and board[r + i + 1][c] == 0):
                            i += 1
                        board[r + i][c] = board[r][c]
                        board[r][c] = 0
        
        crushset = find()
        while (crushset):
            crush(crushset)
            drop()
            crushset = find()
        
        return board

                        
            
            

                    







        
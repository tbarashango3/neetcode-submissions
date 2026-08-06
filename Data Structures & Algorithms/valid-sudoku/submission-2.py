class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        #vertical + horizontal
        for i in range(n):
            #board[0][0], board[1][0], board[0][2]
            horiz = []
            vert = []
            for j in range(n):
                if board[j][i] in vert:
                    return False
                elif board[j][i] != ".":
                    vert.append(board[j][i])
                if board[i][j] in horiz:
                    return False
                elif board[i][j] != ".":
                    horiz.append(board[i][j])
            print(horiz)
        #square
        for square in range(n):
            sq1 = []
            for i in range(0, 3):
                for j in range(0, 3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in sq1:
                        return False
                    else:
                        sq1.append(board[row][col])
        return True
        
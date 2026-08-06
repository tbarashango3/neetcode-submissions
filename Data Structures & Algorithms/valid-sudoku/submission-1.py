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
        sq1 = []
        sq2 = []
        sq3 = []
        sq4 = []
        sq5 = []
        sq6 = []
        sq7 = []
        sq8 = []
        sq9 = []
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in sq1:
                    return False
                else:
                    sq1.append(board[i][j])
            for j in range(3, 6):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in sq2:
                    return False
                else:
                    sq2.append(board[i][j])
            for j in range(6, 9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in sq3:
                    return False
                else:
                    sq3.append(board[i][j])
        #print(sq1)
        for i in range(3, 6):
            for j in range(0, 3):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in sq4:
                    return False
                else:
                    sq4.append(board[i][j])
            for j in range(3, 6):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in sq5:
                    return False
                else:
                    sq5.append(board[i][j])
            for j in range(6, 9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in sq6:
                    return False
                else:
                    sq6.append(board[i][j])
        for i in range(6, 9):
            for j in range(0, 3):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in sq7:
                    return False
                else:
                    sq7.append(board[i][j])
            for j in range(3, 6):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in sq8:
                    return False
                else:
                    sq8.append(board[i][j])
            for j in range(6, 9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in sq9:
                    return False
                else:
                    sq9.append(board[i][j])
        return True
        
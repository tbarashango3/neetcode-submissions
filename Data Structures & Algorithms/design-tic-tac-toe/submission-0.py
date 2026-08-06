class TicTacToe:

    def __init__(self, n: int):
        self.b = [[0 for i in range(n)] for j in range(n)]
        self.moves = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        self.b[row][col] = player
        self.moves += 1
        #print(self.b)
        if self.moves >= self.n * 2 - 1:
            #check vert
            if all(i == player for i in self.b[row]):
                return player
            
            #check horz
            if all(row[col] == player for row in self.b):
                return player

            #check diag
            winDiag1 = True
            for i in range(self.n):
                if self.b[i][i] != player:
                    winDiag1 = False
                    break
            if winDiag1:
                return player
            winDiag2 = True
            for i in range(self.n):
                if self.b[i][self.n - i - 1] != player:
                    winDiag2 = False
                    break
            if winDiag2:
                return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

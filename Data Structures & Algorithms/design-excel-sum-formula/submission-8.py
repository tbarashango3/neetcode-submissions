class Excel:

    def __init__(self, height: int, width: str):
        self.height = height
        self.width = width
        self.mat = [[0 for i in range(height)] for j in range(ord(width) - 64)]
        self.n = {}
        

    def set(self, row: int, column: str, val: int) -> None:
        print("set")
        self.mat[row-1][ord(column) - 65] = val
        #print(self.n)
        if column + str(row) in self.n.keys():
            self.n.pop(column + str(row))
        if len(self.n) > 0:
            for key, value in self.n.items():
                self.sum(int(key[1]), key[0], value)
        print(self.mat)

    def get(self, row: int, column: str) -> int:
        key = column + str(row)
        if key in self.n:
            return self.sum(row, column, self.n[key])
        return self.mat[row-1][ord(column) - 65]

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        self.s = 0
        for num in numbers:
            if len(num) == 2:
                self.s += self.get(int(num[1]), num[0])
            else:
                for i in range(int(num[1]), int(num[4]) + 1):
                    for j in range(ord(num[0]), ord(num[3]) + 1):
                        self.s += self.get(i, chr(j))
        self.mat[row-1][ord(column) - 65] = self.s
        self.n[column + str(row)] = numbers
        print(self.n)
        return self.s


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)

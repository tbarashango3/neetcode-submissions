class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row = len(grid)
        col = len(grid[0])

        rot = set()
        count = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rot.add((i, j))
                elif grid[i][j] == 1:
                    possible = False
                    for dr, dc in directions:
                        r = i + dr
                        c = j + dc
                        if r >= 0 and r < row and c >= 0 and c < col:
                            if grid[r][c] != 0:
                                possible = True
                    if not possible:
                        return -1
        
        while rot:
            print(rot)
            temp = set()
            for rf in rot:
                rr, rc = rf
                for dr, dc in directions:
                        r = rr + dr
                        c = rc + dc
                        if r >= 0 and r < row and c >= 0 and c < col and (r, c):
                            if grid[r][c] == 1:
                                grid[r][c] = 2
                                temp.add((r, c))
            rot = temp
            count += 1
        
        if count == 0:
            return 0
        return count - 1
                        



        
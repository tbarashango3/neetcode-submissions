class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row = len(grid)
        col = len(grid[0])
        q = collections.deque()
        count = 0
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while fresh > 0 and q:
            #print(rot)
            l = len(q)
            for i in range(l):
                rr, rc = q.popleft()
                for dr, dc in directions:
                        r = rr + dr
                        c = rc + dc
                        if r >= 0 and r < row and c >= 0 and c < col and (r, c):
                            if grid[r][c] == 1:
                                grid[r][c] = 2
                                q.append((r, c))
                                fresh-=1
            count += 1
        
        if fresh == 0:
            return count
        return -1
                        



        
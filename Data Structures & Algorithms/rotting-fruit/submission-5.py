class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        queue = deque()
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))

        while queue:
            #print(queue)
            rotted = False
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in neighbors:
                    nr = dr + r
                    nc = dc + c
                    if min(nr, nc) < 0 or nr >= rows or nc >= cols or grid[nr][nc] != 1:
                        continue
                    else:
                        #print("neighbors: ", (nr, nc))
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        rotted = True
            if rotted:
                count += 1
        
        good = False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    good = True
        if good:
            return -1
        return count



        
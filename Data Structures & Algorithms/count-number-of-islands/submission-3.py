class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        neighbors = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def bfs(grid, r, c):
            queue = deque()
            grid[r][c] = "0"
            queue.append((r, c))
            while queue:
                row, col = queue.popleft()
                for dr, dc in neighbors:
                    if (min(row + dr, col + dc) < 0 or len(grid) <= row + dr or len(grid[0]) <= col + dc or grid[row + dr][col + dc] == "0"):
                        continue
                    queue.append((row + dr, col + dc))
                    grid[row + dr][col +dc] = "0"


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(grid, r, c)
                    count += 1
    
        return count

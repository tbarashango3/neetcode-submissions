class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(grid, r, c):
            if min(r, c) < 0 or len(grid) == r or len(grid[0]) == c or grid[r][c] == "0":
                return
            if grid[r][c] == "1":
                grid[r][c] = "0"
            dfs(grid, r-1, c)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)
            dfs(grid, r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(grid, r, c)
        return count

                



        
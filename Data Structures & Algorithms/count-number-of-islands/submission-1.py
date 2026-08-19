class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        col = len(grid[0])
        row = len(grid)
        ans = 0

        def dfs(r, c):
            #print(r, c)
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1
        
        return ans


            

        
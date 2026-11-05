class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in neighbors:
                nr, nc = dr + r, dc + c
                if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)
        
        for i in range(rows):
            dfs(i, 0, pacific)
        for j in range(cols):
            dfs(0, j, pacific)
        for i in range(rows):
            dfs(i, cols - 1, atlantic)
        for j in range(cols):
            dfs(rows - 1, j, atlantic)

        return list(pacific & atlantic)
                




            



        
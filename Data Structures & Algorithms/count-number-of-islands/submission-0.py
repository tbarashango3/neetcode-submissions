class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid[0])
        m = len(grid)
        print(n)
        print(m)
        island = 0
        s = set()
        for i in range(m):
            for j in range(n):
                stack = []
                #print("Set: ", s)
                if grid[i][j] == "1" and (i, j) not in s:
                    island += 1
                    stack.append((i, j))
                while stack:
                    top = stack.pop()
                    if top not in s:
                        s.add(top)
                    if top[0] < m - 1 and grid[top[0] + 1][top[1]] == "1" and (top[0] + 1, top[1]) not in s:
                        stack.append((top[0] + 1, top[1]))
                    if top[0] > 0 and grid[top[0] - 1][top[1]] == "1" and (top[0] - 1, top[1]) not in s:
                        stack.append((top[0] - 1, top[1]))
                    if top[1]  < n - 1 and grid[top[0]][top[1] + 1] == "1" and (top[0], top[1] + 1) not in s:
                        stack.append((top[0], top[1] + 1))
                    if top[1] > 0 and grid[top[0]][top[1] - 1] == "1" and (top[0], top[1] - 1) not in s:
                        stack.append((top[0], top[1] - 1))
        return island


        
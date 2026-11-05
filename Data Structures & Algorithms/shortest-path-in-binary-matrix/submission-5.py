class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        n = len(grid)
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        count = 1
        visited = set()

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        if n and len(grid[0]) == 1:
            return 1

        """
        1. start (0, 0), add (0, 0) to visited, add (0, 0) to queue
        2. queue == (0, 0), count = 1, 
        
        """

        queue.append((0, 0))
        visited.add((0, 0))
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                print(r, c)
                if r == n - 1 and c == n - 1:
                    return count
                for dr, dc in neighbors:
                    nr, nc = dr + r, dc + c
                    if (nr, nc) not in visited and 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        print("new: ", (nr, nc))
            count += 1
        return -1
        
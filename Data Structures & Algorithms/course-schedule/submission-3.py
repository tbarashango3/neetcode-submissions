class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        n = len(prerequisites)
        if n == 0:
            if numCourses >= 1:
                return True
            return False
        for i in range(numCourses):
            adj[i] = []
        for pre, c in prerequisites:
            adj[c].append(pre)

        count = 1

        visited = set()
        path = set()

        def dfs(c):
            if c in path:
                return False
            if c in visited:
                return True
            path.add(c)
            if c in adj:
                for pre in adj[c]:
                    if not dfs(pre):
                        return False
            path.remove(c)
            visited.add(c)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
            

        return True


        
        
    


        

        
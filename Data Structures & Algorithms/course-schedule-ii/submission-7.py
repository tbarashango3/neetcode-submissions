class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        adj = {}
        for i in range(n):
            adj[i] = []
        for pre, c in prerequisites:
            adj[c].append(pre)

        ans = []
        visited = set()
        completed = set()
        #print(adj)
        """
        0 - visited = [0], and = []
        1 - ans = [1], visited 
        
        """

        def dfs(c):
            #print(ans)
            if c in visited:
                return False
            if c in completed:
                return True

            visited.add(c)
            for pre in adj[c]:
                if not dfs(pre):
                    return False
            
            visited.remove(c)
            completed.add(c)
            ans.append(c)
            return True

            
        for i in range(n):
            if not dfs(i):
                return []

        return list(reversed(ans))
        




        
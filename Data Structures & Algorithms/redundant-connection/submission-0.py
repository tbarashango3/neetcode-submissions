class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        n = len(edges)
        for i in range(1, n+1):
            adj[i] = []
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        print(adj)
        
        def dfs(s, graph, visited):
            if s in visited:
                return
            visited.add(s)
            for dest in graph[s]:
                dfs(dest, graph, visited)

        for i in range(n-1, -1, -1):
            visited = set()
            temp = {}
            for node, neighbors in adj.items():
                temp[node] = neighbors[:]
            temp[edges[i][0]].remove(edges[i][1])
            temp[edges[i][1]].remove(edges[i][0])
            dfs(n, temp, visited)
            if len(visited) == n:
                return edges[i]
        return []




        
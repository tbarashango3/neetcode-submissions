class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        ans = []
        for i, equation in enumerate(equations):
            a, b = equation
            if a not in adj:
                adj[a] = []
            if b not in adj:
                adj[b] = []
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        print(adj)
        def dfs(start, target, visited, val):
            #print(start, target)
            visited.add(start)
            if start not in adj or target not in adj:
                return -1.0
            #print(adj[start])
            if start == target:
                return val
            for v in adj[start]:
                if v[0] not in visited:
                    result = dfs(v[0], target, visited, val * v[1])
                    if result != -1.0:
                        return result
            return -1
            
        for first, second in queries:
            visited = set()
            val = 1.0
            #print(first, second, visited, val)
            quotient = dfs(first, second, visited, val)
            ans.append(quotient)
            print(ans)
        
        return ans
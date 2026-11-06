class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        for src, dest, t in times:
            adj[src].append((dest, t))
        
        visited = set()
        minheap = [(0, k)]
        count = 0

        while minheap:
            #print(minheap)
            t1, s1 = heapq.heappop(minheap)
            if s1 in visited:
                continue
            visited.add(s1)
            count = t1

            for d2, t2 in adj[s1]:
                if d2 not in visited:
                    heapq.heappush(minheap, (t1 + t2, d2))
                    #count += 1
        if len(visited) == n:
            return count
        return -1
        



        
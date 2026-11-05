"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        ans = []
        visited = {}
        queue = deque()

        if not node:
            return None

        visited[node] = Node(node.val)
        queue.append(node)
        '''
        1 - queue = 1, visited = 1, add 2 to visited, add 2 to queue, add 2 to ans
        2. - queue = 2, visited = (1, 2), add 3 to visited, add 3 to queue, add 1,3 to ans
        3. - queue = 3, add 2 to ans
        
        '''

        while queue:
            newnode = queue.popleft()
            for n in newnode.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val)
                    queue.append(n)
                
                visited[newnode].neighbors.append(visited[n])

        return visited[node]

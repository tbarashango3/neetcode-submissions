"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:   
    
    def getMin(self, node):
        print("min: ", node.val)
        if not node.left:
            return node
        return self.getMin(node.left)

    def goUp(self, node):
        print("up: ", node.val)
        if node.parent and node == node.parent.left:
            return node.parent
        elif node and node.parent:
            return self.goUp(node.parent)
        else:
            return node.parent
    
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            return self.getMin(node.right)
        return self.goUp(node)

        
    



        
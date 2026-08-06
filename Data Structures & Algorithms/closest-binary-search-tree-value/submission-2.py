# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.d = {}
        def traverse(self, node):
            if not node:
                return False
            self.d[node.val] = abs(node.val - target)
            traverse(self, node.left)
            traverse(self, node.right)
        traverse(self, root)
        print(self.d)
        return min(self.d.items(), key=lambda x: (x[1], x[0]))[0]



        
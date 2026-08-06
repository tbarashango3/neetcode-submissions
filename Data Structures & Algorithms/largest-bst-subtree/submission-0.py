# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if not node:
                return True, 0, float('inf'), float('-inf')
            leftBst, leftSize, leftMin, leftMax = traverse(node.left)
            rightBst, rightSize, rightMin, rightMax = traverse(node.right)

            if leftBst and rightBst and leftMax < node.val < rightMin:
                n = leftSize + rightSize + 1
                self.ans = max(self.ans, n)
                return True, n, min(node.val, leftMin), max(node.val, rightMax)

            return False, 0, 0, 0
        self.ans = 0
        traverse(root)
        return self.ans

        
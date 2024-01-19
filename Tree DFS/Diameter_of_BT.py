# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.diameterAndHeight(root)[0]

    def diameterAndHeight(self, node) -> (int, int):
        if not node:
            return (0, 0)
        leftD, leftH = self.diameterAndHeight(node.left)
        rightD, rightH = self.diameterAndHeight(node.right)
        height = 1 +  max(leftH, rightH)
        diameter = max(leftH + rightH, max(leftD, rightD))
        return (diameter, height)
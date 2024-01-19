# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, acc, path):
            if not node:
                return 
            acc += node.val
            newPath = path + [node.val]
            if (acc == targetSum and not node.left and not node.right):
                res.append(newPath)
                return 
            dfs(node.left, acc, newPath)
            dfs(node.right, acc, newPath)
        dfs(root, 0, [])
        return res
        
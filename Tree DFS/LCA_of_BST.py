class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small = min(p, q, key=lambda x: x.val)
        big = max(p, q, key=lambda x: x.val)
        if not root:
            return None
        elif (root == p or root == q):
            return root
        elif (small.val < root.val < big.val):
            return root
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            return left or right
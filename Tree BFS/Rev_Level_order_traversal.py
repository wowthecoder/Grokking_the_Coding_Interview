from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stack = deque()
        stack.append(root)
        while stack:
            n = len(stack)
            row = []
            for i in range(n):
                node = stack.popleft()
                if node:
                    row.append(node.val)
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
            if row:
                res.append(row)
        res.reverse()
        return res
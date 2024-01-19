class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        rev = False
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
            if rev:
                row.reverse()
            res.append(row)
            rev = not rev
        return res

        
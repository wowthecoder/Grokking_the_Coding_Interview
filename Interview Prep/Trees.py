from collections import deque 

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left 
        self.right = right 

class TreeOp:
    def serializeTree(self, root):
        queue = deque() 
        queue.append(root)
        res = []

        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft() 
                if node:
                    res.append(node.val)
                    # Add into queue even when subtree is null
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append(None)
        
        # Post processing to remove all null childs at the end
        while res and res[-1] is None:
            res = res[:-1]
        return res 
    
    # Testing functions
    def size(self, node):
        if not node: 
            return 0 
        return 1 + self.size(node.left) + self.size(node.right)
    
    def depth(self, node):
        if not node: 
            return 0 
        return 1 + max(self.depth(node.left), self.depth(node.right))
    
    def getBalance(self, node):
        if not node:
            return 0 
        return self.depth(node.left) - self.depth(node.right)
    
    def insert(self, node, val): 
        # Normal BST insertion
        if not node:
            return TreeNode(val)
        if val < node.val: 
            node.left = self.insert(node.left, val)
        else:
            node.right = self.insert(node.right, val)

        # Step 2 - get balance factor
        balance = self.getBalance(node)

        # Step 3 - If the node is unbalanced, then try out the 4 cases
        ## Case 1 - Left left 
        if balance > 1 and val < node.left.val:
            return self.rightRotate(node)
        
        ## Case 2 - Right right
        if balance < -1 and val > node.right.val:
            return self.leftRotate(node)
        
        ## Case 3 - Left right case 
        if balance > 1 and val > node.left.val:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        
        ## Case 4 - Right left case 
        if balance < -1 and val < node.right.val:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        
        return node 

    # Same style as insertion, must balance the tree after standard deletion
    def delete(self):
        return  

    # Utility functions for insert
    # z is the root
    def leftRotate(self, z):
        # If there's an imbalance, the depth will be at least 2 
        # The precondition of leftRotate ensures that Null exception won't be thrown here
        # left rotation is called when right subtree is too deep
        y = z.right 
        T2 = y.left 

        # Perform rotation
        y.left = z 
        z.right = T2 

        # return the new root
        return y
    
    def rightRotate(self, z):
        y = z.left 
        T3 = y.right 

        # Perform rotation
        y.right = z 
        z.left = T3 

        return y

if __name__ == "__main__":
    root = TreeNode(10)
    ops = TreeOp()
    root = ops.insert(root, 3)
    root = ops.insert(root, 1)
    root = ops.insert(root, 7)
    root = ops.insert(root, 17)
    root = ops.insert(root, 8)
    print("Serialized form: ", ops.serializeTree(root))
    print("Number of nodes: ", ops.size(root))
    print("Depth of tree: ", ops.depth(root))
    print("Balance of root(left - right): ", ops.getBalance(root))

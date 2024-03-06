class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    # With path compression optimization
    def find(self, x: int) -> int: 
        # The root of the parent tree
        if (x == self.parent[x]):
            return x 
        # RHS is the recursion, to go up the parent tree to find the root
        # Then move the branch to be a direct child of the root so we don't have to go up 
        # thru the tree all the way again the next time we need the parent of this node
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    # Attach the tree with lower size to bigger size
    # Basically make x and y have the same parent
    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        if x != y: 
            if self.size[x] < self.size[y]:
                # swap x and y
                x, y = y, x 
            self.parent[y] = x 
            self.size[x] += self.size[y]
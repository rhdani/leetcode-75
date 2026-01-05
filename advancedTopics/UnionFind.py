class UnionFind:

    # Initializing the parent list and count variable by traversing the grid
    def __init__(self, grid):
        self.parent = []
        self.rank = []
        self.count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" or grid[i][j] == 1:
                    self.parent.append(i * n + j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    # Function to find the root parent of a node
    def find(self, i):
        # Treat -1 (water / invalid node) specially
        if i < 0 or i >= len(self.parent) or self.parent[i] == -1:
            return -1
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # Function to connect components
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        # If either is water/invalid, skip union
        if root_x == -1 or root_y == -1 or root_x == root_y:
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        self.count -= 1

    # Function to return the number of conencted components consisting of "1"s
    def get_count(self):
        return self.count

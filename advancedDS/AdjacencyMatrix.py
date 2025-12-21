from collections import deque

class AdjacencyMatrix:
    def __init__(self, n, directed=False):
        """
        Initializes an N x N matrix with zeros.

        :param n: Number of nodes in the graph.
        :param directed: Boolean, True if the graph is directed, False otherwise.
        """
        self.n = n
        self.directed = directed
        # Initialize the matrix with zeros using list comprehension
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]

    def add_edge(self, u, v, weight=1):
        """
        Adds an edge from node u to node v.

        :param u: Source node index (0 to N-1).
        :param v: Destination node index (0 to N-1).
        :param weight: The value to store (default is 1 for unweighted).
        """
        if 0 <= u < self.n and 0 <= v < self.n:
            self.matrix[u][v] = weight

            # If undirected, the connection goes both ways
            if not self.directed:
                self.matrix[v][u] = weight
        else:
            raise IndexError("Node index out of range.")

    def isEdge(self, u, v):
        if (self.matrix[u][v] == 1):
            return True
        return False

    def getNeighbors(self, nodeIndex) -> list:
        retVal = []
        if nodeIndex > self.n:
            return retVal
        for i in range(self.n):
            if (self.matrix[nodeIndex][i] == 1):
                retVal.append(i)
        return retVal

    def remove_edge(self, u, v):
        """Removes the edge between u and v by setting it to 0."""
        self.add_edge(u, v, weight=0)

    def display(self):
        """Prints the matrix in a readable format."""
        print(f"Adjacency Matrix ({'Directed' if self.directed else 'Undirected'}):")
        for row in self.matrix:
            print("  ".join(map(str, row)))

    def is_connected(self, u, v):
        """
        Returns True if there is a path from node u to node v.
        Uses Breadth-First Search (BFS).
        """
        # 1. Basic bounds check
        if not (0 <= u < self.n and 0 <= v < self.n):
            return False

        # 2. If u and v are the same node, they are connected
        if u == v:
            return True

        # 3. BFS Traversal
        visited = [False] * self.n
        queue = deque([u])
        visited[u] = True

        while queue:
            current_node = queue.popleft()

            # Check all possible neighbors in the matrix
            for neighbor in range(self.n):
                # If there is an edge and we haven't visited this node yet
                if self.matrix[current_node][neighbor] != 0 and not visited[neighbor]:
                    if neighbor == v:
                        return True
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False


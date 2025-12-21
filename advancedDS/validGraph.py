def valid_graph(n, edges):
    """
    n: int - number of nodes
    edges: List[List[int]] - list of edges where each edge is represented as a pair [u, v]
    Returns True if the edges form a valid tree with n nodes, False otherwise.
    This approach uses DFS to check for cycles and connectivity. And goes through all edges.
    """
    if (len(edges) != n - 1):
        return False
    visited = set()
    visited.add
    nodeStack = [0]

    while nodeStack:
        node = nodeStack.pop()
        visited.add(node)
        for edge in edges:
            u, v = edge
            if u == node and v not in visited:
                nodeStack.append(v)
            elif v == node and u not in visited:
                nodeStack.append(u)
    return len(visited) == n

# Driver code
def main():
    n = [3, 4, 5, 5, 6]
    edges = [[[0, 1], [0, 2], [1, 2]],
             [[0, 1], [0, 2], [0, 3]],
             [[0, 1], [0, 2], [0, 3], [0, 4], [3, 4]],
             [[0, 1], [0, 2], [0, 3], [3, 4]],
             [[0, 1], [0, 2], [1, 3], [2, 4], [0, 5]]]

    for i in range(len(n)):
        print(i + 1, ".\t n = ", n[i], sep="")
        print("\t Edges = ", edges[i], sep="")
        print("\t Is the given graph a valid tree:", valid_graph(n[i], edges[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()


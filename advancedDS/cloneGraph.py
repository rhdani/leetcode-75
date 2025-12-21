class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

def clone(root):
    if root is None:
        return None
    mapping = {root: Node(root.data)}
    stack = [root]
    while stack:
        node = stack.pop()
        for nei in node.neighbors:
            if nei not in mapping:
                mapping[nei] = Node(nei.data)
                stack.append(nei)
            mapping[node].neighbors.append(mapping[nei])
    return mapping[root]

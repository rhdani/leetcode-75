from Node import *

def create_graph(data):
    if len(data) == 0:
        return Node(1)
    nodes = []
    for i in range(len(data)):
        nodes.append(Node(i+1))
    
    for i, node in enumerate(nodes):
        for neighbor in data[i]:
            node.neighbors.append(nodes[neighbor-1])
    return nodes[0] 

def create_2D_list(root):
    queue = [root]
    visited = {}
    graph = []
    node_index = {}

    while queue:
        node = queue.pop(0)
        neighbors = []

        for neighbor in node.neighbors:
            neighbors.append(visited.get(neighbor, neighbor).data)
            if neighbor not in visited and neighbor not in queue:
                visited[neighbor] = neighbor
                queue.append(neighbor)

        neighbors.sort()

        if node not in node_index:
            node_index[node] = len(graph)
            graph.append([node.data, neighbors])
        else:
            graph[node_index[node]][1] = neighbors

    graph.sort(key=lambda x: x[0])
    
    return [sublist[1] for sublist in graph]

def print_graph_rec(root, visited_nodes):
    if root == None or root in visited_nodes:
        return

    visited_nodes.add(root)
    print("\t", str(root.data), end = ": {")
    for n in root.neighbors:
        print(str(n.data), end = " ")
    print("}")

    for n in root.neighbors:
        print_graph_rec(n, visited_nodes)

def print_graph(root):
    visited_nodes = set()
    print_graph_rec(root, visited_nodes)

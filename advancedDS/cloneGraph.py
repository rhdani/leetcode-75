from Node import *
from graph_utility import *

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

# Driver code
def main():
    data = [[[2, 3], [1, 3], [1, 2]],
            [[2, 4], [1, 3], [2, 4], [1, 3]],
            [[2, 5], [1, 3], [2, 4], [3, 5], [1, 4]],
            [[2], [1]],
            [[2, 6], [1, 3], [2, 4], [3, 5], [4, 6], [1, 5]],
            [[]]
            ]

    for i in range (len(data)):
      node1 = create_graph(data[i])
      print(i+1, ".\t Original Graph: ", create_2D_list(node1), "\n", sep="")
      print_graph(node1)
      print()
      cloned_root = clone(node1)
      print("\t Cloned Graph: ", create_2D_list(cloned_root), "\n", sep="")
      print_graph(node1)
      print("-"*100)  

main()

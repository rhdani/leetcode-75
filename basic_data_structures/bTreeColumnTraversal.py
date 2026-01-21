from collections import deque, defaultdict
from TreeNode import *
from BinaryTree import *

def vertical_order(root):

    if root is None:
        return None

    col_map = defaultdict(list)
    queue = deque([(root, 0)])   # (node, column)

    min_col = max_col = 0

    while queue:
        node, col = queue.popleft()

        col_map[col].append(node.data)
        min_col = min(min_col, col)
        max_col = max(max_col, col)

        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))

    return [col_map[c] for c in range(min_col, max_col + 1)]

# Driver code
if __name__ == '__main__':
    
    list_of_trees = [
        [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(75), TreeNode(300), TreeNode(10), TreeNode(350), TreeNode(15)],
        [TreeNode(20), TreeNode(40), TreeNode(50), TreeNode(90), TreeNode(67), TreeNode(94)],
        [TreeNode(-10), TreeNode(-23), TreeNode(45), TreeNode(25), TreeNode(46)],
        [TreeNode(9), TreeNode(7), None, None, TreeNode(1), TreeNode(8), TreeNode(10), None, TreeNode(12)],
        [TreeNode(3), TreeNode(2), TreeNode(3), None, TreeNode(3), None, TreeNode(1)]
    ]

    input_trees = []
    for list_of_nodes in list_of_trees:
        tree = BinaryTree(list_of_nodes)
        input_trees.append(tree)

    x = 1
    for tree in input_trees:
        print(x, ".\tInput Tree:", sep = "")
        tree.display_tree()
        x += 1
        print("\n\tVertical order traversal: ", vertical_order(tree.root), sep="")
        print("-" * 100)

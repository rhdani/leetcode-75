from TreeNode import *
from BinaryTree import *

class Solution:
    def lowest_common_ancestor(self, current_node, p, q):
        if (current_node is None):
            return None
        if (current_node.data == p.data or current_node.data == q.data):
            return current_node
        left_ancestor = right_ancestor = None
        if (current_node.left != None):
            left_ancestor = self.lowest_common_ancestor(current_node.left, p, q)
        if (current_node.right != None):
            right_ancestor = self.lowest_common_ancestor(current_node.right, p, q)
        if (left_ancestor != None and right_ancestor != None):
            return current_node
        if (not left_ancestor and not right_ancestor):
            return None
        if (left_ancestor != None):
            return left_ancestor
        else:
            return right_ancestor

# driver code
def main():
    input_trees = [[TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(75), TreeNode(350)],
        [TreeNode(100), TreeNode(200), TreeNode(75), TreeNode(50), TreeNode(25), TreeNode(350)],
        [TreeNode(350), TreeNode(100), TreeNode(75), TreeNode(50), TreeNode(200), TreeNode(25)],
        [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(75), TreeNode(350)],
        [TreeNode(25), TreeNode(50), TreeNode(75), TreeNode(100), TreeNode(200), TreeNode(350)]]

    input_nodes = [
        [25, 75],
        [50, 350],
        [100, 200],
        [50, 25],
        [350, 200]
    ]

    for i in range(len(input_trees)):
        solution = Solution()
        tree = BinaryTree(input_trees[i])
        print(i+1, ".\tBinary tree:", sep="")
        tree.display_tree()
        print("\tp = ", input_nodes[i][0])
        print("\tq = ", input_nodes[i][1])
        lca = solution.lowest_common_ancestor(tree.root, tree.find(input_nodes[i][0]), tree.find(input_nodes[i][1]))
        print("\n\tLowest common ancestor: ", lca.data, sep="")
        print("-"*100)

if __name__ == "__main__":
    main()


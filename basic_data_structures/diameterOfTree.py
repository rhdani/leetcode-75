from BinaryTree import *
from TreeNode import TreeNode
'''
Docstring for diameterOfTree
Given a binary tree, you need to compute the length of the tree’s diameter. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
'''

def diameter_of_binaryTree(root):
    max_diameter = 0

    def depth(node):
        nonlocal max_diameter
        if not node:
            return 0
        
        left_depth = depth(node.left)
        right_depth = depth(node.right)

        # Update the maximum diameter found so far
        max_diameter = max(max_diameter, left_depth + right_depth)

        # Return the depth of the tree rooted at this node
        return max(left_depth, right_depth) + 1

    depth(root)
    return max_diameter

# Driver code
def main():
    list_of_trees = [ [TreeNode(2), TreeNode(1), TreeNode(4), TreeNode(3), TreeNode(5), TreeNode(6), TreeNode(7)],
                    [TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)],
                    [TreeNode(45), TreeNode(32), TreeNode(23), TreeNode(21), TreeNode(18), TreeNode(1)],
                    [TreeNode(5), TreeNode(3), TreeNode(4), TreeNode(1), TreeNode(2), TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)],
                    [TreeNode(-1), TreeNode(-5), TreeNode(-8), TreeNode(-3), TreeNode(1), TreeNode(5), TreeNode(3)],
                    [TreeNode(9), TreeNode(7), None, None, TreeNode(1), TreeNode(8), TreeNode(10), None, TreeNode(12)]
    ]

    input_trees = []
    for list_of_nodes in list_of_trees:
        tree = BinaryTree(list_of_nodes)
        input_trees.append(tree)

    y = 1
    for tree in input_trees:
        print(y, ".\tInput Tree:", sep = "")
        tree.display_tree()
        #display_tree(tree.root)
        print("\tDiameter of the tree: ", diameter_of_binaryTree(tree.root), sep="")
        print("-"*100)
        y += 1

if __name__ == '__main__':
    main()
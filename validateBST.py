from TreeNode import *
from BinaryTree import *

'''
Alternate implementation using recursion
def validate_bst_helper(node, value):
    if not node:
         return True

    if not validate_bst_helper(node.left, value):
        return False

    if node.data <= value[0]:
        return False
    value[0] = node.data

    return validate_bst_helper(node.right, value)
    
def validate_bst(root):
    
    prev = [float('-inf')]
    
    return validate_bst_helper(root, prev)

'''
def validate_bst(root):

    prev = float('-inf')

    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if (curr.data <= prev):
            return False
        prev = curr.data
        curr = curr.right

    return True

# Driver code
def main():
    list_of_trees = [ [TreeNode(5), TreeNode(3), TreeNode(2), TreeNode(6), TreeNode(4)],
                    [TreeNode(6), TreeNode(2), TreeNode(5), TreeNode(4), TreeNode(7)],
                    [TreeNode(4), TreeNode(2), TreeNode(5), TreeNode(1), TreeNode(3)],
                    [TreeNode(7), TreeNode(2), TreeNode(5), TreeNode(4), TreeNode(8)],
                    [TreeNode(9), TreeNode(5), TreeNode(7), TreeNode(1), TreeNode(3)],
                    [TreeNode(5), TreeNode(3), TreeNode(8), TreeNode(2), TreeNode(4), None, TreeNode(9)]
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
        print("\n\tValid BST: ", validate_bst(tree.root), sep = "")
        print("-" * 100)

if __name__ == '__main__':
    main()


'''
Docstring for smartRobber
A thief has discovered a new neighborhood to target, 
where the houses can be represented as nodes in a binary tree. 
The money in the house is the data of the respective node. 
The thief can enter the neighborhood from a house represented 
as root of the binary tree. Each house has only one parent house. 
The thief knows that if he robs two houses that are directly connected, 
the police will be notified. The thief wants to know the maximum 
amount of money he can steal from the houses without getting 
caught by the police. The thief needs your help determining the 
maximum amount of money he can rob without alerting the police.
'''

from TreeNode import TreeNode
from BinaryTree import BinaryTree   

def helper(node):
    if not node:
        return (0, 0)
    left_rob, left_not = helper(node.left)
    right_rob, right_not = helper(node.right)
    rob = node.data + left_not + right_not
    not_rob = max(left_rob, left_not) + max(right_rob, right_not)
    return (rob, not_rob)


def rob(root):
    rob_val, not_rob_val = helper(root)
    return max(rob_val, not_rob_val)

if __name__ == '__main__':
    
    # Create a list of list of TreeNode objects to represent binary trees
    list_of_trees = [ [TreeNode(10), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)],
                    [TreeNode(7), TreeNode(9), TreeNode(10), TreeNode(15), TreeNode(20)],
                    [TreeNode(8), TreeNode(2), TreeNode(17), TreeNode(1), TreeNode(4), TreeNode(19), TreeNode(5)],
                    [TreeNode(7), TreeNode(3), TreeNode(4), TreeNode(1), TreeNode(3)],
                    [TreeNode(9), TreeNode(5), TreeNode(7), TreeNode(1), TreeNode(3)],
                    [TreeNode(9), TreeNode(7), None, None, TreeNode(1), TreeNode(8), TreeNode(10), None, TreeNode(12)]
    ]

    # Create the binary trees using the BinaryTree class
    input_trees = []
    for list_of_nodes in list_of_trees:
        tree = BinaryTree(list_of_nodes)
        input_trees.append(tree)

    # Print the input trees
    x = 1
    for tree in input_trees:
        print(x, ".\tInput Tree:", sep = "")
        tree.display_tree()
        x += 1
        print("\tMaximum amount we can rob without getting caught: ", rob(tree.root), sep = "")
        print("-" * 100)
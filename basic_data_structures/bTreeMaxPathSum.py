from BinaryTree import *
from TreeNode import TreeNode

def helper_f(root, maxSum):
    if (not root):
        return 0
    max_left = helper_f(root.left, maxSum)
    max_right = helper_f(root.right, maxSum)
    #Contrib from left and right sub trees
    left_subtree = right_subtree = 0
    if (max_left > 0):
        left_subtree = max_left
    if (max_right > 0):
        right_subtree = max_right
    value_new_path = root.data + left_subtree + right_subtree
    maxSum[0] = max(maxSum[0], value_new_path)
    return (root.data + max(left_subtree, right_subtree))
    
def max_path_sum(root):
    max_sum = float('-inf')
    maxSum = [max_sum]*1
    helper_f(root, maxSum)
    return maxSum[0]

# Driver code
def main():
    input_trees = [
        [TreeNode(-8), TreeNode(2), TreeNode(17), TreeNode(1), TreeNode(4), TreeNode(19), TreeNode(5)],
        [TreeNode(7), TreeNode(3), TreeNode(4), TreeNode(-1), TreeNode(-3)],
        [TreeNode(-10), TreeNode(9), TreeNode(20), TreeNode(30), TreeNode(16), TreeNode(15), TreeNode(7)],
        [TreeNode(1),TreeNode(2),TreeNode(3)],
        [TreeNode(0)],
        [TreeNode(-10), TreeNode(9), TreeNode(20), None, None, TreeNode(15), TreeNode(7)],
        [TreeNode(1), TreeNode(-3),TreeNode(3), TreeNode(5), None, None, TreeNode(-5)]
    ]

    indx = 1
    for i in input_trees:
        tree = BinaryTree(i)
        print(indx, ".\tBinary Tree:", sep="")
        indx += 1
        tree.display_tree()
        print("\n\t Maximum path sum:\t", max_path_sum(tree.root))
        print("\n", "-"*100)

if __name__ == '__main__':
    main()

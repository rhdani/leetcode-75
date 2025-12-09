from TreeNode import *
from BinaryTree import *

def same_tree(p, q):

    if (not p and not q):
        return True
    if (p and q and p.data != q.data):
        return False
    if (p and not q):
        return False
    if (q and not p):
        return False
    if (p.data == q.data):
        return (same_tree(p.left, q.left) and same_tree(p.right, q.right))
    else:
        return False
    return False
# Driver code
def main():
    input_p = [[TreeNode(3), TreeNode(9), TreeNode(10), None, None, TreeNode(5), TreeNode(6)], [TreeNode(3), TreeNode(9), TreeNode(10), None, None, TreeNode(5), TreeNode(6)], [TreeNode(1), TreeNode(2), None, TreeNode(4), TreeNode(5)], [TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), None, TreeNode(8)], [TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)]]
    input_q = [[TreeNode(3), TreeNode(9), TreeNode(10), None, None, TreeNode(5), TreeNode(6)], [TreeNode(3), TreeNode(9), TreeNode(10), None, None, TreeNode(6), TreeNode(5)], [TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)], [TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), None, TreeNode(8)], [TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)]]
    for i in range(len(input_p)):
        root_p = BinaryTree(input_p[i])
        root_q = BinaryTree(input_q[i])
        print(str(i + 1) + ". First Binary tree:")
        root_p.display_tree()
        print("   Second Binary tree:")
        root_q.display_tree()
        print("   Are the trees same:", same_tree(root_p.root, root_q.root))
        print("-" * 100, "\n", sep="")


if __name__ == "__main__":
    main()


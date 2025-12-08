from TreeNode import *
from BinaryTree import *

def mirror_binary_tree(root):
 
  if root == None:
    return None
  if (root.left != None):
    ltree = mirror_binary_tree(root.left)
  if (root.right != None):
    rtree = mirror_binary_tree(root.right)
  tmp = root.right
  root.right = root.left
  root.left = tmp
  return root

# Driver code
def main():

    input_trees = [
        [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(75), TreeNode(125), TreeNode(350)],
        [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(110), TreeNode(125), TreeNode(350)],
        [TreeNode(100), TreeNode(50), TreeNode(200), TreeNode(25), TreeNode(75), TreeNode(90), TreeNode(350)],
        [TreeNode(25), TreeNode(50), TreeNode(75), TreeNode(100), TreeNode(125), TreeNode(350)],
        [TreeNode(350), TreeNode(125), TreeNode(100), TreeNode(75), TreeNode(50), TreeNode(25)],
        [TreeNode(100)],
        [TreeNode(1), TreeNode(2), None, TreeNode(3), None, TreeNode(4)],
        [TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), None, None, TreeNode(5)],
        []
    ]

    indx = 1
    for i in input_trees:
        tree = BinaryTree(i)

        print(indx, ".\tBinary Tree:", sep="")
        indx += 1
        tree.display_tree()
        mirror_binary_tree(tree.root)
        print("\n\tMirrored binary tree:")
        tree.display_tree()
        print("-"*100)

if __name__ == '__main__':
    main()


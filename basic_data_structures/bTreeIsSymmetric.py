from collections import deque
from BinaryTree import *
from TreeNode import *

def is_symmetric(root):

  myq = deque()
  if not root:
    return True
  myq.append(root.left)
  myq.append(root.right)
  
  while len(myq) > 0:
    left = myq.popleft()
    right = myq.popleft()
    
    if left is None and right is None:
      continue
    if left is None and right is not None:
      return False
    if right is None and left is not None:
      return False
    if left.data != right.data:
      return False
    myq.append(left.left)
    myq.append(right.right)
    myq.append(left.right)
    myq.append(right.left)
    
  return True

# Driver code
def main():
  list_of_trees = [[TreeNode(1), TreeNode(2), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(4), TreeNode(3)],
  [TreeNode(18), TreeNode(21), TreeNode(21), TreeNode(47), TreeNode(20), TreeNode(21), TreeNode(47)],
  [TreeNode(25), TreeNode(4), TreeNode(67), TreeNode(2), TreeNode(3), TreeNode(3), TreeNode(2)],
  [TreeNode(1), TreeNode(2), TreeNode(2), TreeNode(3), None, None, TreeNode(3)],
  [TreeNode(1), TreeNode(2), TreeNode(2), None, TreeNode(3), TreeNode(3), None, TreeNode(4), TreeNode(5), TreeNode(5), TreeNode(4)]]

  input_trees = []
  for list_of_nodes in list_of_trees:
    tree = BinaryTree(list_of_nodes)
    input_trees.append(tree)
  
  i = 0
  for tree in input_trees:
    print(i+1,".\tInput Tree: ")
    tree.display_tree()
    print("\n\tResult:", is_symmetric(tree.root))
    print("-"*100)
    i+=1

if __name__ == '__main__':
    main()

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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


from queue import Queue
from TreeNode import *

class BinaryTree:
    """
    Manages the overall Binary Tree structure and display logic.
    The constructor takes a list of Node objects and links them using the 
    standard level-order index-based relationship (like a complete binary tree).
    """
    def __init__(self, nodes):
        self.root = None
        if not nodes:
            return
        self.root = self.createBinaryTree(nodes)

    def createBinaryTree(self, nodes):
        if len(nodes) == 0:
            return None

        # Create the root node of the binary tree
        root = TreeNode(nodes[0].data)

        # Create a queue and add the root node to it
        queue = Queue()
        queue.put(root)

        # Start iterating over the list of nodes starting from the second node
        i = 1
        while i < len(nodes):
            # Get the next node from the queue
            curr = queue.get()

            # If the node is not None, create a new TreeNode object for its left child,
            # set it as the left child of the current node, and add it to the queue
            if nodes[i] is not None:
                curr.left = TreeNode(nodes[i].data)
                queue.put(curr.left)

            i += 1

            # If there are more nodes in the list and the next node is not None,
            # create a new TreeNode object for its right child, set it as the right child
            # of the current node, and add it to the queue
            if i < len(nodes) and nodes[i] is not None:
                curr.right = TreeNode(nodes[i].data)
                queue.put(curr.right)

            i += 1

        # Return the root of the binary tree
        return root
    
    def find_helper(self, node, value):
        if node == None:
            return None
        if (node.data == value):
            return node
        retVal = None
        if (node.left != None):
            retVal = self.find_helper(node.left, value)
        if (retVal != None):
            return retVal
        if (node.right != None):
            retVal =  self.find_helper(node.right, value)
        return retVal
        
    def find(self, value):
        if not self.root:
            return None
        if (self.root.data == value):
            return self.root
        if (self.root.left != None):
            retVal = self.find_helper(self.root.left, value)
        if (retVal != None):
            return retVal
        if (self.root.right != None):
            retVal =  self.find_helper(self.root.right, value)
        return retVal
             
    def display_tree(self):
        """
        Prints the tree structure as ASCII text, level by level.
        Uses Level-Order Traversal (BFS).
        """
        if not self.root:
            print("Tree is empty.")
            return

        # Queue for Breadth-First Search (BFS)
        queue = [self.root]
        
        # We will use 'None' as a level delimiter and 'x' for null nodes 
        # to ensure correct spacing.
        # Max nodes at depth D is 2^D. We stop when a level is all None/null nodes.
        
        current_level_nodes = [self.root]
        
        while any(current_level_nodes):
            level_output = []
            next_level_nodes = []
            
            # 1. Process the current level
            for node in current_level_nodes:
                if node:
                    # Append the node's data
                    level_output.append(str(node.data))
                    
                    # Add children for the next level's processing
                    next_level_nodes.append(node.left)
                    next_level_nodes.append(node.right)
                else:
                    # Append a placeholder 'x' for null nodes for spacing
                    level_output.append('x')
                    
                    # We still need to account for the 'null' node's potential
                    # children to maintain the structure (they will be null too)
                    next_level_nodes.append(None)
                    next_level_nodes.append(None)

            # Check if all remaining nodes are None (i.e., we've hit the leaves)
            if all(n is None for n in next_level_nodes):
                break
                
            # 2. Print the level output
            print(" ".join(level_output))
            
            # 3. Prepare for the next iteration
            current_level_nodes = next_level_nodes
        
        # Print the final level (which was processed before the break)
        print(" ".join([str(n.data) if n else 'x' for n in current_level_nodes if any(current_level_nodes)]))

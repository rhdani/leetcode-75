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

        # The input list is treated as a level-order representation of a
        # complete binary tree (using array-based indexing).
        self.root = nodes[0]

        for i, node in enumerate(nodes):
            if node is not None:
                # Calculate indices for children
                left_idx = 2 * i + 1
                right_idx = 2 * i + 2

                # Assign left child
                if left_idx < len(nodes) and nodes[left_idx] is not None:
                    node.left = nodes[left_idx]

                # Assign right child
                if right_idx < len(nodes) and nodes[right_idx] is not None:
                    node.right = nodes[right_idx]

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


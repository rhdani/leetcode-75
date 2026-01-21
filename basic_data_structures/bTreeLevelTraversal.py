from collections import deque
from TreeNode import *
from BinaryTree import *

def level_order_traversal(root):
    if (root == None):
        return "None"
    current_queue = deque()
    next_queue = deque()
    level = 0
    current_queue.append(root)
    result = ""
    
    while (current_queue):
        node = current_queue.popleft()
        result += str(node.data)
        if (node.left):
            next_queue.append(node.left)
        if (node.right):
            next_queue.append(node.right)
        
        if (len(current_queue) == 0):
            level = level + 1
            if (next_queue):
                result += " : "
            current_queue, next_queue = next_queue, current_queue
        else:
            result += ", "
    
    return result
def main():
    test_cases_roots = []

    input1 = [
        TreeNode(100),
        TreeNode(50),
        TreeNode(200),
        TreeNode(25),
        TreeNode(75),
        TreeNode(350)
    ]
    tree1 = BinaryTree(input1)
    test_cases_roots.append(tree1)

    input2 = [
        TreeNode(25),
        TreeNode(50),
        None,
        TreeNode(100),
        TreeNode(200),
        TreeNode(350)
    ]
    tree2 = BinaryTree(input2)
    test_cases_roots.append(tree2)

    input3 = [
        TreeNode(350),
        None,
        TreeNode(100),
        None,
        TreeNode(50),
        TreeNode(25)
    ]
    tree3 = BinaryTree(input3)
    test_cases_roots.append(tree3)

    tree4 = BinaryTree([TreeNode(100)])
    test_cases_roots.append(tree4)

    #test_cases_roots.append(None)

    for i in range(len(test_cases_roots)):
        if i > 0:
            print()
        print(i + 1, ".\tBinary Tree")
        test_cases_roots[i].display_tree()
        print("\n\tLevel order traversal: ")
        print("\t",level_order_traversal(test_cases_roots[i].root))
        print("\n" + '-' * 100)


if __name__ == '__main__':
    main()

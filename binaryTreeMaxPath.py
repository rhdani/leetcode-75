# Definition of a binary tree node
#
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(p_order, i_order):

    if (len(p_order) == 0 or len(i_order) == 0):
        return None
    inorder_hash_map = {value: index for index, value in enumerate(i_order)}

    length = len(i_order)
    root = TreeNode(p_order[0])
    ind = inorder_hash_map[p_order[0]]
    left_inorder = i_order[:ind]
    right_inorder = i_order[ind+1:]
    l1 = len(left_inorder)
    left_preorder = p_order[1:l1+1]
    right_preorder = p_order[l1+1:]
    root.left = build_tree(left_preorder, left_inorder)
    root.right = build_tree(right_preorder, right_inorder)

    return root

# Driver code
def main():

    p_order = [
        [3, 9, 20, 15, 7],
        [-1],
        [10, 20, 40, 50, 30, 60],
        [1, 2, 4, 5, 3, 6],
        [1, 2, 4, 7, 3],
        [1, 2, 4, 8, 9, 5, 3, 6, 7]

    ]
    i_order = [
        [9, 3, 15, 20, 7],
        [-1],
        [40, 20, 50, 10, 60, 30],
        [4, 2, 5, 1, 6, 3],
        [4, 2, 7, 1, 3],
        [8, 4, 9, 2, 5, 1, 6, 3, 7]
    ]

    indx = 0
    for i in range(len(p_order)):

        print(indx+1, ".\tPre order: ", p_order[indx], sep="")
        print("\tIn order: ", i_order[indx], sep="")
        tr = build_tree(p_order[indx], i_order[indx])
        indx += 1
        print("\n\tBinary tree:")
        #display_tree(tr)
        print("-"*100)
if __name__ == '__main__':
    main()


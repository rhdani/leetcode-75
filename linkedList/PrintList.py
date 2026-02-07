from ListNode import *
# Template for printing the linked list with forward arrows

def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.val, end=" ")  # print node value

        temp = temp.next
        if temp:
            print("→", end=" ")
        else:
            # if this is the last node, print null at the end
            print("→ null", end=" ")


def print_grid(grid):
    """Print a 2-D matrix (list of lists) to stdout.

    Each row is printed on its own line with elements separated by a single space.
    The function returns None.
    """
    if grid is None:
        print(None)
        return

    for row in grid:
        if row is None:
            print()
            continue
        print(" ".join(str(x) for x in row))


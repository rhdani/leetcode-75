from LinkedList import *
from ListNode import *
from PrintList import *

'''
Fold a linked list by reversing the second half and merging it with the first half.
'''
def reorder_list(head):
    if head is None or head.next is None:
        return head

    # Find the end of first half (slow)
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Split the list into two halves
    second = slow.next
    slow.next = None

    # Reverse the second half
    prev = None
    curr = second
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second = prev

    # Merge the two halves
    first = head
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2

    return head

def main():
    input_list = [
        [1, 1, 2, 2, 3, -1, 10, 12],
        [10, 20, -22, 21, -12],
        [1, 1, 1],
        [-2, -5, -6, 0, -1, -4],
        [3, 1, 5, 7, -4, -2, -1, -6]
    ]

    # Additional edge-case tests
    # empty list -> should remain empty
    # single node -> should remain the same
    # two nodes -> should swap into folded order (first, second)
    input_list.extend([
        [],
        [42],
        [1, 2]
    ])

    for i, inp in enumerate(input_list):
        obj = LinkedList()
        obj.create_linked_list(inp)

        print(i + 1, ".\tOriginal list: ", end="", sep="")
        print_list_with_forward_arrow(obj.head)

        obj.head = reorder_list(obj.head)

        print("\n\tAfter folding: ", end="")
        print_list_with_forward_arrow(obj.head)
        if i != len(input_list) - 1:
            print("\n", "-"*100, sep="")


if __name__ == '__main__':
    main()

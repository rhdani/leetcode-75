from ListNode import *
from LinkedList import *
from PrintList import *

def reverse(head):

    prev = None
    curr = head
    next = None
    while (curr):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
        
    return head


def main():
    input = (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1],
        [10],
        [1, 2],
    )

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(i+1, ".\tInput linked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tReversed linked list: ", end="")
        print_list_with_forward_arrow(reverse(input_linked_list.head))
        print("\n", "-"*100)


if __name__ == "__main__":
    main()

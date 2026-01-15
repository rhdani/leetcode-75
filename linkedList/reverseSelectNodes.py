from LinkedList import *
from ListNode import *
from PrintList import *

'''
Reverse even length groups in a linked list.
Given the head of a linked list, the nodes in it are assigned to each group in a sequential manner. 
The length of these groups follows the sequence of natural numbers. 
Natural numbers are positive whole numbers denoted by
(1,2,3,4...).

In other words:

The 1st node is assigned to the first group.
The 2nd and 3rd nodes are assigned to the second group.
The 4th, 5th, and 6th nodes are assigned to the third group, and so on.

Your task is to reverse the nodes in each group with an even number of nodes and return the head of the modified linked list.

'''
def reverse_even_length_groups(head):
  groupLength = 1
  prev = None
  curr = head

  while curr is not None:
    # count how many nodes are actually available in this group (up to groupLength)
    count = 0
    temp = curr
    while temp is not None and count < groupLength:
      temp = temp.next
      count += 1

    # ptr to node before this group
    ptrToPrevGroupEnd = prev

    if count % 2 == 0:
      # reverse 'count' nodes
      tail_of_group = curr
      n = 0
      while n < count and curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        n += 1

      # connect previous part to new head of this group
      if ptrToPrevGroupEnd is not None:
        ptrToPrevGroupEnd.next = prev
      else:
        # reversed at head
        head = prev

      # connect tail to the next node after the group
      tail_of_group.next = curr
      # prev should point to tail_of_group for next iteration
      prev = tail_of_group
    else:
      # skip these 'count' nodes (no reversal)
      i = 0
      while i < count and curr is not None:
        prev = curr
        curr = curr.next
        i += 1

    groupLength += 1

  return head

# Driver Code

def to_list(head):
    lst = []
    temp = head
    while temp:
        lst.append(temp.data)
        temp = temp.next
    return lst


def main():
    input = [
        [1, 2, 3, 4],
        [10, 11, 12, 13, 14],
        [15],
        [16, 17]
    ,
      [],
      [1, 2],
      [1, 2, 3, 4, 5, 6, 7, 8, 9],
      [2, 4, 6, 8, 10, 12],
      [1, 2, 3, 4, 5, 6]
    ]

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(
            i+1, ".\tIf we reverse the even length groups of the linked list: ", end='\n\t', sep="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\n\tWe will get: ", end='\n\t')
        print_list_with_forward_arrow(
            reverse_even_length_groups(input_linked_list.head))
        print("\n", "-" * 100)


if __name__ == '__main__':
    main()
import math
from LinkedList import LinkedList
from ListNode import ListNode
from PrintList import print_list_with_forward_arrow

def merge_2_lists(list1, list2):
    dummy = ListNode(0)
    curr = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    curr.next = list1 or list2
    return dummy.next

def merge_k_lists(lists):
    
    num_lists = len(lists)
    
    if (num_lists == 0 or (num_lists == 1)):
        return lists
    
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(merge_2_lists(l1, l2))
        lists = merged
    
    return lists[0]
    
# Driver code
def main():
    inputlists = [[[21, 23, 42], [1, 2, 4]],
        [[11, 41, 51], [21, 23, 42]],
        [[2], [1, 2, 4], [25, 56, 66, 72]],
        [[11, 41, 51], [2], [2], [2], [1, 2, 4]],
        [[10, 30], [15, 25], [1, 7], [3, 9], [100, 300], [115, 125], [10, 70], [30, 90]]
    ]
    inp_num = 1
    for i in inputlists:
        print(inp_num, ".\tInput lists:", sep = "")
        ll_lists = []
        for x in i:
            a = LinkedList()
            a.create_linked_list(x)
            ll_lists.append(a.head)
            print("\t", end = "")
            print_list_with_forward_arrow(a.head)
            print()
        inp_num += 1
        print("\tMerged list: \n\t", end = "")
        print_list_with_forward_arrow(merge_k_lists(ll_lists))
        print("\n", "-"*100, sep = "")

if __name__ == "__main__":
    main()

import heapq
from LinkedList import LinkedList
from ListNode import ListNode
from PrintList import print_list_with_forward_arrow

def merge_k_lists(lists):
    min_heap = []
    
    # Initialize the heap with the first element of each list
    for i in range(len(lists)):
        if lists[i]:  # Check if the list is not empty
            heapq.heappush(min_heap, (lists[i].val, 0, i, lists[i]))  # (value, list index, element index)
    
    merged_list = []
    
    while min_heap:
        value, element_index, list_index, list_node = heapq.heappop(min_heap)
        merged_list.append(value)
        
        # If there is a next element in the same list, add it to the heap
        if list_node.next:
            list_node = list_node.next
            next_tuple = (list_node.val, element_index + 1, list_index, list_node)
            heapq.heappush(min_heap, next_tuple)
    
    return merged_list

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
        print(merge_k_lists(ll_lists))
        print("\n", "-"*100, sep = "")

if __name__ == "__main__":
    main()

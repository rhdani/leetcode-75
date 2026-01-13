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

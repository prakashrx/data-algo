def get_middle_node(head):
    
    slow = head
    fast =  head.next

    while fast is not None:
        slow = slow.next
        fast = fast.next
        if fast is not None:
            fast = fast.next

    return slow.data

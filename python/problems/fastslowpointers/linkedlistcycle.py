from linked_list import LinkedList

def detect_cycle(head):
    if head is None:
        return False
    slow = head
    fast = head.next

    while fast is not None  and  fast != slow:
        slow = slow.next
        fast = fast.next
        if fast is not None:
            fast = fast.next

    return True if fast is not None else False
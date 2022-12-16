def palindrome(head):

    slow = head
    stack.append(slow.data)
    fast = head.next
    stack = []
    even = False
    while fast is not None:
        slow = slow.next
        stack.append(slow.data)
        fast = fast.next
        if fast is not None:
            fast = fast.next
        else:
            even = True
    if not even:
        stack.pop()

    slow = slow.next
    while slow is not None:
        if slow.data != stack.pop():
            return False
        slow = slow.next
    return True

        
    

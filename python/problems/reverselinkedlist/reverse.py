from linked_list import LinkedList

def reverse(head):
    cur = head
    prev = None
    while cur is not None:
        t = cur.next
        cur.next = prev
        prev = cur
        cur = t

    return prev



lst = LinkedList()
lst.create_linked_list([1,-2,3,4,-5,4,3,-2,1])
reverse(lst.head)
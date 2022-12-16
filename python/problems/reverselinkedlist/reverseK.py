from linked_list import LinkedList, print_linked_list

def reverse(head, k):
    cur = head
    c = 0
    while cur is not None and c < k:
        cur = cur.next
        c = c + 1
    if c < k:
        return (head, None)

    cur = head
    prev = None
    c = 0

    while cur is not None and c < k:
        t = cur.next
        cur.next = prev
        prev = cur
        cur = t
        c = c + 1

    return (prev, cur)

def reverse_linked_list(head, k):
  
    last = head
    (head, cur) = reverse(head, k)
    while cur:
        t = cur
        (h, cur) = reverse(cur, k)
        last.next = h
        last = t

    return head

lst = LinkedList()
lst.create_linked_list([1,2,3,4,5])
print_linked_list(reverse_linked_list(lst.head, 2))
from linked_list import LinkedList, print_linked_list

def reverse(head, k):

    prev = None
    cur = head
    c = 0
    while cur and c < k:
        t = cur.next
        cur.next = prev
        prev = cur
        cur = t
        c += 1
    return (prev,cur)

def reverse_between(head, left, right):

    cur = head
    prev = None
    c = 1
    while cur and c < left:
        prev = cur
        cur = cur.next
        c += 1
    
    (h,n) =  reverse(cur, right - left + 1)
    if prev:
        prev.next = h
    else:
        head = h
    cur.next = n
    return head






lst = LinkedList()
lst.create_linked_list([1,2,3,4,5])
print_linked_list(lst.head)
print_linked_list(reverse_between(lst.head, 1,9))
#print_linked_list(reverse(lst.head.next, 2)[0])
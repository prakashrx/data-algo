from linked_list import LinkedList, LinkedListNode, print_linked_list


def reverse_even(head, k): 
    cur = head
    c = 0
    while cur and c < k:
        c += 1
        cur = cur.next
    cur = head
    prev = None
    if c % 2 == 0:
        c = 1
        while cur and c<= k:
            t = cur.next
            cur.next = prev
            prev = cur
            cur = t
            c += 1
        return (prev, cur, True)
    else:
        c = 1
        while cur and c <= k:
            prev = cur
            cur = cur.next
            c += 1
        return (head, cur, False)


def reverse_even_length_groups(head):
    c = 1
    cur = head
    prev = None
    while cur:
        (h, n, rev) =  reverse_even(cur, c)
        if rev:
            if prev:
                prev.next = h
            cur.next = n
        prev = cur
        cur = n
        c += 1

    return head




def test(arr):
    lst = LinkedList()
    lst.create_linked_list(arr)
    print_linked_list(reverse_even_length_groups(lst.head))

test([1, 2, 3, 4])
test([11, 12, 13, 14, 15])


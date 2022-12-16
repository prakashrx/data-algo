from linked_list import LinkedList,print_linked_list

def swap_nodes(head, k):

    cur = head
    c = 1
    while cur and c < k:
        cur = cur.next
        c += 1
    
    start = cur
    end = head
    while cur.next:
        end = end.next
        cur = cur.next

    start.data, end.data = end.data, start.data
    return head


lst = LinkedList()
lst.create_linked_list([10, 7, 15, 17, 10, 0, 2, 13, 46, 1, 0, 22, 8])

print_linked_list(swap_nodes(lst.head, 9))
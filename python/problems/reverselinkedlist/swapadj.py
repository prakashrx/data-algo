from linked_list import LinkedList, LinkedListNode, print_linked_list

def swap_pair(head):
    first = head
    second = first.next
    if not second:
        return (first, None)
    
    t = second.next
    second.next = first
    first.next = None

    return (second, t)


def swap_pairs(head):
    prev = head
    (head, cur) = swap_pair(head)
    while cur:
        (lst, next) = swap_pair(cur)
        prev.next = lst
        prev = cur
        cur = next
    return head



def test(arr):
    lst = LinkedList()
    lst.create_linked_list(arr)
    print_linked_list(swap_pairs(lst.head))
    

test([1,2,3,4])
test([10,1,2,3,4,5])
test([28,21,14])
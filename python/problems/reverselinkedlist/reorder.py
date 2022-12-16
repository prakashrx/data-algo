from linked_list import LinkedList, LinkedListNode, print_linked_list

def find_middle(head):
    prev = None
    slow = head
    fast = head.next
    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next
    return (slow, prev)

def reverse(head):
    
    prev = None
    cur = head
    while cur:
        t = cur.next
        cur.next = prev
        prev = cur
        cur = t
    return prev


def reorder_list(head):

    (middle, last) = find_middle(lst.head)
    last.next = None
    list1 = head
    list2 = reverse(middle)
    newlst = LinkedListNode(0)
    cur = newlst
    while list1 or list2:
        if list1:
            cur.next = list1
            list1 = list1.next
            cur = cur.next
        if list2:
            cur.next = list2
            list2 = list2.next
            cur = cur.next
    return newlst.next

lst = LinkedList()
lst.create_linked_list([1,1,2,2,3,-1,10,12])
print_linked_list(reorder_list(lst.head))



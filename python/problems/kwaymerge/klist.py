
from linked_list import LinkedList, LinkedListNode, print_linked_list

# Tip: You may use some of the code templates provided
# in the support files
def merge_list(list1, list2):
    head1,head2 = list1,list2
    dummy = LinkedListNode(0)
    cur = dummy
    while head1 or head2:
        if head1 and head2:
            if head1.data < head2.data:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
        elif head1:
            cur.next = head1
            head1 = head1.next
        else:
            cur.next = head2
            head2 = head2.next
        cur = cur.next

    return dummy.next

def merge_k_lists(lists):
    list = lists[0].head
    for i in  range(1, len(lists)):
        list = merge_list(list, lists[i].head)
    return list
    


lst1 = LinkedList().create_linked_list([21,23,42])
lst2 = LinkedList().create_linked_list([1,2,4])
lst3 = LinkedList().create_linked_list([5,10,15])
print_linked_list(merge_k_lists([lst1, lst2, lst3]))
# 206. Reverse Linked List

from myLinkedList import ListNode, create_linked_list, show_linked_list


def reverseList(head: ListNode) -> ListNode:
    node     = head
    new_head = None
    new_tail = None
    stack = []
    while node is not None:
        stack.append(node)
        node = node.next
    while stack:
        if new_head is None:
            new_head = stack.pop()
            new_tail = new_head
        else:
            new_tail.next = stack.pop()
            new_tail      = new_tail.next
    
    if new_tail:
        new_tail.next = None
    return new_head


head_1 = create_linked_list([1,2,3,4,5])
head_2 = create_linked_list([1,2])
head_3 = create_linked_list([])

head_R = reverseList(head_1)
head_2 = reverseList(head_2)
head_3 = reverseList(head_3)

show_linked_list(head_R)
show_linked_list(head_2)
show_linked_list(head_3)

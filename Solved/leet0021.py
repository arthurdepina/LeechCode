# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    tail = dummy = ListNode()  # Por que é necessário criar o dummy?

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            # Não entendi por que a linha acima é assim.
            # Por que não tail.val = list1.val
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    tail.next = list1 if list1 else list2

    return dummy.next

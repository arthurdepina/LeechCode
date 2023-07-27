# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:  # while they're not empty
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        # At the end of the while loop above, at least one of the lists will be empty
        if list1:  # If list1 is not empty
            tail.next = list1
        elif list2:  # If list2 is not empty
            tail.next = list2

        return dummy.next

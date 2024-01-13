# 002. Add two numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list = ListNode()
        current = new_list
        carry = 0 
        while l1 or l2 or carry:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            new_val      = val_1 + val_2 + carry
            carry        = new_val // 10
            new_val      = new_val % 10
            current.next = ListNode(new_val)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return new_list.next
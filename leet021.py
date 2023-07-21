# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(list1, list2):
    if len(list1) > len(list2):
        upper_bound = len(list1)
    else:
        upper_bound = len(list2)
    k = 0
    i = 0
    j = 0
    output = list()
    while k < upper_bound:
        if i == len(list1) or j == len(list2):
            break
        if list1[i] < list2[j]:
            output[k] = list[i]
        else:
            output[k] = list[j]
        k += 1


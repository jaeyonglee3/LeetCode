# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2

        # fakenode will always point to head while result moves around
        # so the two only point to the same node initially
        res = fakenode = ListNode()

        while curr1 and curr2:
            if curr1.val < curr2.val:
                res.next = curr1
                curr1 = curr1.next
            else:
                res.next = curr2
                curr2 = curr2.next
            
            res = res.next
        
        if curr1:
            res.next = curr1
        elif curr2:
            res.next = curr2
        
        return fakenode.next
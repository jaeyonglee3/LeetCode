# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        dummy_head = dummy_curr = ListNode()

        while curr1 and curr2:
            if curr1.val < curr2.val:
                dummy_curr.next = curr1
                curr1 = curr1.next
            else:
                dummy_curr.next = curr2
                curr2 = curr2.next
            
            dummy_curr = dummy_curr.next
        
        if curr1:
            dummy_curr.next = curr1
        if curr2:
            dummy_curr.next = curr2
        
        return dummy_head.next
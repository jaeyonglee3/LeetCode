# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        # a node with default value serves as the head of the result
        res_head = res_curr = ListNode()

        while curr1 and curr2:
            if curr1.val < curr2.val:
                res_curr.next = curr1
                curr1 = curr1.next
            else:
                res_curr.next = curr2
                curr2 = curr2.next
            
            res_curr = res_curr.next
        
        if curr1:
            res_curr.next = curr1
        elif curr2:
            res_curr.next = curr2
        
        return res_head.next
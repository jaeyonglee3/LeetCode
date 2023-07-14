# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()  # dummy always points to the head 
        # curr moves along the merged list adding new nodes.
        # dummy and curr refer to the same object in memory initially. 

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                curr.next = list1
                list1, curr = list1.next, curr.next
            else:
                curr.next = list2
                list2, curr = list2.next, curr.next
        
        if list1 or list2:
            curr.next = list1 if list1 else list2
        
        return dummy.next  # dummy.next points to the head of the merged list. 
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Need to keep track of previous, current, and head

        prev = None
        curr = head

        while curr:
            original_next = curr.next
            curr.next = prev
            prev = curr
            curr = original_next
        
        return prev

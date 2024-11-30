# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            old_next = curr.next # save the next node
            curr.next = prev # change the next to point to prev node
            prev = curr
            curr = old_next
        
        # prev is the head of the reversed linkedlist
        return prev
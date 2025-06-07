# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # step 1: compute the length
        tail, curr = None, head
        list_len = 0
        while curr:
            list_len += 1
            tail, curr = curr, curr.next
        
        # compute modulo operation
        rotations = k % list_len
        if rotations == 0:
            return head

        tail.next = head
        # the new head will be at index length - rotations
        prev, curr = None, head
        for _ in range(list_len - rotations):
            prev = curr
            curr = curr.next
        
        prev.next = None
        return curr

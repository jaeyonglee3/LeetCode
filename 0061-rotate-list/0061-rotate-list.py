# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base cases:
        if not head or not head.next or k == 0:
            # if empty, nothing to rotate
            # if a single node, any k applied has no effect
            # if k == 0, no rotations at all are applied
            return head
        
        # step 1: compute the length
        tail, curr = None, head
        list_len = 0
        while curr:
            list_len += 1
            tail, curr = curr, curr.next
        
        # step 2: compute effective number of rotations
        rotations = k % list_len
        if rotations == 0:
            return head

        # step 3: temporarily make the list circular
        tail.next = head

        # step 4: go to the new head and break the cycle
        # the new head will be at index length - rotations
        # return this new head after cycle is broken
        prev, curr = None, head
        for _ in range(list_len - rotations):
            prev = curr
            curr = curr.next
        prev.next = None  # breaks the cycle

        return curr  # because curr points to the new head now

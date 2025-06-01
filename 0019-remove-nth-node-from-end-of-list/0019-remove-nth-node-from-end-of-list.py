# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if we have the total # of nodes, the nth node from the end is equal to the
        # (total - n + 1)th node from the front

        # first, get the total # of nodes
        total = 0
        curr = head
        while curr:
            total += 1
            curr = curr.next
        
        # edge case: if first node needs to be removed, just return head.next
        if n == total: return head.next
        
        # now, remove the (total - n + 1)th node from the front
        to_remove = total - n + 1
        curr, prev = head, None
        i = 1

        while i < to_remove:
            prev = curr
            curr = curr.next
            i += 1
        
        prev.next = curr.next
        return head


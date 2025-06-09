# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        l, r = head, head.next
        new_head = head.next

        prev_pair_tail = None
        while r:
            old_r_nxt = r.next

            l.next = r.next
            r.next = l

            if prev_pair_tail:
                prev_pair_tail.next = r
            prev_pair_tail = l

            l = old_r_nxt
            r = l.next if l else None
        
        return new_head
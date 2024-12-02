# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head
        num_nodes = 0

        while curr:
            num_nodes += 1
            curr = curr.next
        
        prev, curr = None, head
        curr_n = num_nodes
        curr_i = 0

        while curr_n != n:
            curr_i += 1
            prev = curr
            curr = curr.next
            curr_n = num_nodes - curr_i
        
        # Once loop completes, curr is at nth from end, prev is at (n - 1)th from end
        if prev:
            prev.next = curr.next
            dummy = head
        else:
            # The node being removed is the head
            dummy = curr.next

        return dummy
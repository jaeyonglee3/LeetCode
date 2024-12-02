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

        # Calculate number of nodes
        while curr:
            num_nodes += 1
            curr = curr.next
        
        # Iterate curr to be at nth node from the end, prev to be at (n-1)th from the end
        prev, curr = None, head
        curr_n = num_nodes
        curr_i = 0

        while curr_n != n:
            curr_i += 1
            prev = curr
            curr = curr.next
            curr_n = num_nodes - curr_i
        
        # Make prev point to curr's next node
        # dummy can point to original head
        if prev:
            prev.next = curr.next
            dummy = head
        # Else: The node being removed is the head. 
        # Simply make dummy be the 2nd node in the linkedlist
        else:
            dummy = curr.next

        return dummy
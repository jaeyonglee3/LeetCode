# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # calculate total number of nodes
        # total - n = the node number (from the front) we need to delete

        curr = head
        total = 0
        while curr:
            total += 1
            curr = curr.next
        node_num = total - n
        
        prev, curr = None, head
        for _ in range(node_num):
            prev = curr
            curr = curr.next
        
        if prev:
            prev.next = curr.next
        else:
            return curr.next
        
        return head

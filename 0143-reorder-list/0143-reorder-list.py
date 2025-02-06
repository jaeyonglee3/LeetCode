# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Use slow, fast, prev pointers
        slow = head
        fast = head.next

        while slow:
            prev = None

            while fast and fast.next:
                prev = fast
                fast = fast.next
            
            if prev:
                prev.next = None
                slow_next_old = slow.next
                slow.next = fast
                
                fast.next = slow_next_old
                slow = slow_next_old

                # eventually fast becomes none when slow and prev are next to each other
                fast = slow.next  
            else:
                return
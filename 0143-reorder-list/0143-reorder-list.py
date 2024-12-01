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
        slow, fast = head, head.next

        while slow:
            prev = None

            while fast and fast.next:
                prev = fast
                fast = fast.next

            if prev:
                old_slow_next = slow.next
                slow.next = fast
                
                slow = old_slow_next
                fast.next = slow
                prev.next = None
                fast = slow.next
            else:
                return

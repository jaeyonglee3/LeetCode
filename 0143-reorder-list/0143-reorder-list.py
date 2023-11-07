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
        # Approach 1: Store linkedlist in an array (uses extra space)
        # llist = []

        # curr = head
        # while curr:
        #     llist.append(curr)
        #     curr = curr.next
        
        # l, r = 0, len(llist) - 1

        # while l < r:
        #     llist[l].next = llist[r]
        #     l += 1
        #     llist[r].next = llist[l]
        #     r -= 1
        
        # llist[l].next = None

        #------------------------------------------------
        # Approach 2: (doesn't use any extra memory)
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Now reverse linkedlist from slow to fast window
        # Increment slow once more to include in portion to reverse
        slow = slow.next
        
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        
        # At this point, the 2nd half of the linkedlist has been reversed
        # fast may be None or the last node of the origin LL
        
        left, right = head, prev
        while right and left:
            left_temp = left.next
            left.next = right
            left = left_temp

            right_temp = right.next
            right.next = left
            right = right_temp
        
        left.next = None

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
        if head.next == None: return
        # step 1: find the middle
        # step 2: split the linked list into 2 halves (the middle node will be the starting node for the 2nd half)
        # step 3: reverse the 2nd half
        # step 4: combine the two halves together and return the head

        # step 1
        middle, fast = head, head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                # middle now points to the correct middle
                break
            middle = middle.next
        
        # step 2
        # now middle is the starting node for the 2nd half
        curr = head
        while curr:
            if curr.next == middle:
                curr.next = None
                break
            curr = curr.next

        # step 3
        curr, prev = middle, None
        while curr:
            old_next = curr.next
            curr.next = prev
            prev = curr
            curr = old_next
        
        # step 4
        # now 'prev' is the head to the reversed 2nd half
        curr1, curr2 = head, prev
        while curr1 and curr2:
            tmp1 = curr1.next
            tmp2 = curr2.next

            curr1.next = curr2
            if tmp1 is None:
                break
            curr2.next = tmp1

            curr1 = tmp1
            curr2 = tmp2

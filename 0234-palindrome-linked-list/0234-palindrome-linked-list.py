# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # list is odd length, fast points to middle element
        # list is even length, slow points to the start of section 2
        # reverse the list starting at slow ptr
        prev, curr = None, slow
        while curr:
            old_next = curr.next
            curr.next = prev
            prev = curr
            curr = old_next
        
        # compare the reversed section (starting at prev)
        # to the original head of the linkedlist
        curr1, curr2 = head, prev
        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False
            curr1, curr2 = curr1.next, curr2.next
        
        return True
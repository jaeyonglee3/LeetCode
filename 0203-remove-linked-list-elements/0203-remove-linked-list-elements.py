# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return head
        
        prev, curr = None, head
        new_head = head

        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                if curr == new_head:
                    new_head = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        
        return new_head

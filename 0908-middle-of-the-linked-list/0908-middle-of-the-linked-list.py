# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow advances one node at a time. fast advances two nodes at a time. 
        # This means: By the time fast reaches the end of the list, slow will have reached the middle.
        slow, fast = head, head

        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
            else:
                return slow
        
        return slow
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Have two pointers and update one w a delay of n steps 
        temp = ListNode(0, head)
        curr, curr_delayed = temp, temp

        for _ in range(n):
            curr = curr.next
        
        while curr.next:
            curr, curr_delayed = curr.next, curr_delayed.next

        # At this point, curr_delayed refers to the node before the one to delete
        if curr_delayed.next is None:
            curr_delayed.next = None
        else:
            curr_delayed.next = curr_delayed.next.next

        return temp.next
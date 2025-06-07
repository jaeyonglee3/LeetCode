# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # construct two new linkedlists, 1 and 2
        # then connect them and return the head of smaller
        head1 = curr1 = ListNode()
        head2 = curr2 = ListNode()

        curr = head
        while curr:
            old_next = curr.next
            curr.next = None  # remove curr's next ptr
            
            if curr.val < x:
                curr1.next = curr
                curr1 = curr1.next
            else:
                curr2.next = curr
                curr2 = curr2.next
            
            curr = old_next
        
        # connect the two LinkedLists by making the tail of head1
        # point to the head of head2 (head2.next to skip dummy head)
        curr1.next = head2.next

        # return head1's next to skip the dummy head
        return head1.next
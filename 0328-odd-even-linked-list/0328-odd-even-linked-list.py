# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # similar approach to 86. Partition List
        # we'll create two new LinkedLists, 1st stores odd indices, 2nd stores even.
        # make the tail of the first one point to the head of the second one, 
        # then return head of 1st one. Manipulate ptrs of existing nodes, create 0 new nodes for O(1) space.
        # Code passes through LL once, processing each node once, for O(n) time

        if not head or not head.next:
            return head
        
        curr1 = head  # odd nodes
        head2 = curr2 = head.next  # even nodes

        while curr2 and curr2.next:
            curr1.next = curr2.next
            curr1 = curr1.next

            curr2.next = curr1.next if curr1 else None
            curr2 = curr1.next if curr1 else None
        
        curr1.next = head2  # make tail of head1 point to head of head2
        return head
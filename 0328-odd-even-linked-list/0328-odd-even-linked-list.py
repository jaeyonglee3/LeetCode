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
        
        head1 = curr1 = ListNode()  # stores odd nodes
        head2 = curr2 = ListNode()  # stores even nodes

        curr = head
        i = 1
        while curr:
            old_next = curr.next
            curr.next = None  # remove the old ptr for the node

            if i % 2 != 0:
                curr1.next = curr
                curr1 = curr1.next
            else:
                curr2.next = curr
                curr2 = curr2.next
            
            curr = old_next
            i += 1
        
        curr1.next = head2.next  # make tail of head1 point to head of head2
        return head1.next
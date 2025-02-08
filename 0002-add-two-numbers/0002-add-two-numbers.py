# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        dummy_head = dummy_curr = ListNode()
        is_carry = False

        while curr1 or curr2:
            curr1_val = 0 if not curr1 else curr1.val
            curr2_val = 0 if not curr2 else curr2.val

            result = (curr1_val + curr2_val)
            if is_carry:
                is_carry = False
                result += 1
            
            if result > 9:
                result = result % 10
                is_carry = True
    
            new_node = ListNode(result)
            dummy_curr.next = new_node

            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            dummy_curr = dummy_curr.next
        
        if is_carry:
            dummy_curr.next = ListNode(1)

        return dummy_head.next

# The time complexity of this solution is O(max(N, M)), 
# where N and M are the lengths of l1 and l2. 
# This is because we traverse both linked lists once, 
# processing each node in a single pass.

# The space complexity is also O(max(N, M)) since we 
# create a new linked list to store the sum, 
# with at most one extra node for a carry at the end.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        result = curr = ListNode()
        carry = 0

        while curr1 or curr2:
            curr1_val = curr1.val if curr1 else 0
            curr2_val = curr2.val if curr2 else 0
            
            total = curr1_val + curr2_val + carry
            carry = 0 if total < 10 else 1

            curr.next = ListNode(total % 10)
            curr = curr.next

            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        
        if carry: 
            curr.next = ListNode(carry)
        
        return result.next
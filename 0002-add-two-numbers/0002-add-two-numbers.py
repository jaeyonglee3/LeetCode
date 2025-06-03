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

        while curr1 and curr2:
            total = curr1.val + curr2.val + carry
            carry = 0 if total < 10 else 1

            if total == 10:
                carry = 1

            curr.next = ListNode(total % 10)
            curr = curr.next

            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr1:
            total = curr1.val + carry
            carry = 0 if total < 10 else 1
            curr.next = ListNode(total % 10)
            curr = curr.next
            curr1 = curr1.next
        
        while curr2:
            total = curr2.val + carry
            carry = 0 if total < 10 else 1
            curr.next = ListNode(total % 10)
            curr = curr.next
            curr2 = curr2.next
        
        if carry: 
            curr.next = ListNode(carry)
        
        return result.next
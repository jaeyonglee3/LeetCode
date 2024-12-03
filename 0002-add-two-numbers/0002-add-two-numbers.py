# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        res = curr_res = ListNode()
        carry = False

        while curr1 and curr2:
            new_val = curr1.val + curr2.val

            if carry:
                new_val += 1
                carry = False

            if (new_val % 10 != new_val):
                new_val = new_val % 10
                carry = True
            
            curr_res.next = ListNode(val=new_val)
            curr_res = curr_res.next

            curr1 = curr1.next
            curr2 = curr2.next
        
        if curr1 or curr2 or carry:
            remaining = curr1 if curr1 else curr2
            while remaining or carry:
                if carry and not remaining:
                    curr_res.next = ListNode(val=1)
                    carry = False
                else:
                    new_val = remaining.val + 1 if carry else remaining.val
                    curr_res.next = ListNode(val=new_val % 10)

                    if (new_val % 10 != new_val):
                        new_val = new_val % 10
                        carry = True
                    else:
                        carry = False
                    
                    curr_res = curr_res.next
                    remaining = remaining.next

        return res.next

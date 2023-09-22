# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        bin_num = []

        while curr is not None:
            bin_num.append(curr.val)
            curr = curr.next

        dec_num = 0
        for idx, num in enumerate(bin_num):
            power = len(bin_num) - idx - 1
            dec_num += num * (2 ** power)
        
        return dec_num
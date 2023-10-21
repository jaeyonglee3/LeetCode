# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        visited = []

        if head is None:
            return False

        while curr.next is not None:
            visited.append(curr)

            if curr.next in visited:
                return True
            else:
                curr = curr.next
        
        return False

        # NEXT STEP - this is very slow. optimize w/ two pointer approach.
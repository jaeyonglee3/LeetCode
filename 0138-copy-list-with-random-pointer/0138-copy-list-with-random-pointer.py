"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        curr = head
        copies = {}

        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            new_copy = copies[curr]

            if curr.next:
                new_copy.next = copies[curr.next]

            if curr.random:
                new_copy.random = copies[curr.random]
            
            curr = curr.next
        
        return copies[head]
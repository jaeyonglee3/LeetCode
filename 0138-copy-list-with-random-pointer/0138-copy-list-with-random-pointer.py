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
        # a hashmap would allow us to map the OG node to a copy we create
        # we can implement this fn by doing two passes of the OG linkedlist
        # once to create all the copies, populate a hashmap
        # then again to assign all the random and next ptrs using the hasmap
        old_to_new = {None : None}

        # 1st pass
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        # 2nd pass
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]
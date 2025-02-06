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
        # None always maps to none, so no need to worry about trying to find the
        # value when the key may be null
        old_to_new = {None : None}

        # First, make a copy of every node and store it in old_to_new hashmap
        # where the original node maps to the newly created copy
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        # Then, iterate over each OG node again and for its counterpart in hashmap,
        # assign its next and random pointers to the other values in the hashmap
        curr = head
        while curr:
            new_copy = old_to_new[curr]
            new_copy.next = old_to_new[curr.next]
            new_copy.random = old_to_new[curr.random]
            
            curr = curr.next
        
        # Return the copy associated with the head
        return old_to_new[head]
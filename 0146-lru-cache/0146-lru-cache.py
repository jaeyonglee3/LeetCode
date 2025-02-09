class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # Implemented with doubly linked list and hashmap
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # maps key to node, i.e. value is a ptr to node
        
        # Initialize dummy nodes for pointing to LRU and most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        # Remove from the list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        # Insert at right
        prev, nxt = self.right.prev, self.right
        # insert the node between prev and nxt
        prev.next = node
        nxt.prev  = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # Must also update the node to most recent
            # remove it, then reinsert it
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from linkedlist and delete/evict the LRU from hashmap (cache)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
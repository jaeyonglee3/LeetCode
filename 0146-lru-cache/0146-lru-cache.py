class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        # dummy nodes for lru and mru
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)

        self.lru.next, self.mru.prev = self.mru, self.lru
    
    def insert(self, node):
        prev_mru = self.mru.prev
        prev_mru.next = node
        node.prev = prev_mru
        self.mru.prev = node
        node.next = self.mru

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        # if key does not exist, return -1
        # o/w return the value associated w/ the key
        # then, make that node become the mru
        if key not in self.cache:
            return -1
        
        value = self.cache[key].val
        self.remove(self.cache[key])
        self.insert(self.cache[key])

        return value

    def put(self, key: int, value: int) -> None:
        # if key in cache, update the value
        # o/w add the new key value pair to the cache
        # if number of keys exceeds capacity, evict lru
        if key in self.cache:
            self.remove(self.cache[key])
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > self.cap:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# to get in constant time, we should use a hashmap
# where the keys are the key passed in, and values point to a node in the DLL

# we need a doubly LL b/c we frequently reorder the nodes in the cache
# e.g. everytime we call "get" on some value, it becomes the most recently used
# get(): need a quick way to return a value if the given key exists -> hashmap,
# where the keys are the keys provided during put(), the value will be some kind of node.

# put(): Updating the value of the key, or adding it if it doesn't exist is simple.

# Challenge: if we exceed capacity, the LRU key needs to be evicted. This means ALWAYS keeping
# track of what the least recently used key was. Each time get() is called, that key becomes
# the most recently used. When its immediately added by put(), its the MRU

# Design: each LRU cache will consist of a DLL, where the head points to the LRU and the tail
# points to the MRU. Also, a hashmap will map keys to values, where values are nodes in the DLL
class CacheNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodes = {}

        self.head = CacheNode(None, None)
        self.tail = CacheNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            self.remove(node)
            self.insert(node)
            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            self.remove(node)
            self.insert(node)
            node.val = value
            return
        
        # cap would be exceeded so remove LRU
        if len(self.nodes) + 1 > self.cap:
            lru_node = self.head.next
            del self.nodes[lru_node.key]
            self.remove(lru_node)
        
        # add the key value pair to the cache
        new_node = CacheNode(key, value)
        self.insert(new_node)

        # add to the hashmap
        self.nodes[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
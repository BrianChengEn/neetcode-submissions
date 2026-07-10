class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.pre = self.left
    
    def remove(self, node):
        node_pre = node.pre
        node_next = node.next

        node_pre.next = node_next
        node_next.pre = node_pre
    
    def insert(self, node):
        last_node = self.right.pre

        last_node.next = node
        node.pre = last_node

        node.next = self.right
        self.right.pre = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

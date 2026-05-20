class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dummy_left = Node(0, 0)
        self.dummy_right = Node(0, 0)
        self.dummy_left.next = self.dummy_right
        self.dummy_right.prev = self.dummy_left

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node: Node) -> None:
        node.next = self.dummy_right
        node.prev = self.dummy_right.prev
        node.prev.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            node = self.dummy_left.next
            self.remove(node)
            del self.cache[node.key]
        

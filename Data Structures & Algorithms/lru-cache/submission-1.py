from typing import Optional

class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dummy_l = Node(0, 0)
        self.dummy_r = Node(0, 0)
        self.dummy_l.next = self.dummy_r
        self.dummy_r.prev = self.dummy_l

    def remove(self, node):
        curr = node
        key = curr.key
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

    def insert(self, node):
        self.dummy_l.next.prev = node
        node.next = self.dummy_l.next
        self.dummy_l.next = node
        node.prev = self.dummy_l

        
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
            node = self.dummy_r.prev
            self.remove(node)
            del self.cache[node.key]

        
        

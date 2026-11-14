class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mapping = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node): 
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next, node.prev = None, None
        

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        node = self.mapping[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            node = self.mapping[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.mapping) == self.cap:
                delnode = self.head.next
                del self.mapping[delnode.key]
                self.remove(delnode)
            node = Node(key, value)
            self.mapping[key] = node
            self.insert(node)

          


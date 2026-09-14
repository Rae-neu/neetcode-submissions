class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict()

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev = self.right.prev

        node.prev = prev
        node.next = self.right

        prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        node = self.dic[key]

        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.value = value

            self.remove(node)
            self.insert(node)

        else:
            node = Node(key, value)
            self.dic[key] = node

            self.insert(node)
            
        if len(self.dic) > self.capacity:
            target = self.left.next

            self.remove(target)
            del self.dic[target.key] 
        


class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # left = LRU, right = MRU
        self.left.next = self.right
        self.right.prev = self.left

    # Insert immediately before right (MRU)
    def insert(self, node):
        prev = self.right.prev
        nextn = self.right

        prev.next = node
        nextn.prev = node

        node.prev = prev
        node.next = nextn

    # Remove a node from the list
    def remove(self, node):
        prev = node.prev
        nextn = node.next

        prev.next = nextn
        nextn.prev = prev

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

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

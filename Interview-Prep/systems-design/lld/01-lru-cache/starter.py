"""LRU Cache — fill in the TODOs. Hand-roll hashmap + doubly linked list.
Run: python3 starter.py
"""


class Node:
    __slots__ = ("key", "val", "prev", "next")

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}                 # key -> Node
        # TODO: set up sentinel head/tail nodes and link them
        # self.head <-> self.tail  (head.next is MRU side, tail.prev is LRU side)

    # --- helpers ---
    def _remove(self, node):
        ...  # TODO: unlink node from the list

    def _add_front(self, node):
        ...  # TODO: insert node right after head (most-recently-used)

    # --- API ---
    def get(self, key):
        ...  # TODO: if present, move to front and return val; else -1

    def put(self, key, value):
        ...  # TODO: update or insert; evict from tail if over capacity


if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    print(c.get(1))   # 1   (1 is now MRU)
    c.put(3, 3)       # evicts key 2 (LRU)
    print(c.get(2))   # -1
    c.put(4, 4)       # evicts key 1
    print(c.get(1))   # -1
    print(c.get(3))   # 3
    print(c.get(4))   # 4

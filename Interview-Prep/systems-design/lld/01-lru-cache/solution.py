"""LRU Cache — reference solution.  Run: python3 solution.py
Two implementations: (1) hand-rolled hashmap + doubly linked list (what an
interviewer usually wants), (2) the OrderedDict shortcut.
"""
from collections import OrderedDict


# ---------- (1) Hand-rolled: hashmap + doubly linked list ----------
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
        self.map = {}                      # key -> Node, O(1) lookup
        # Sentinel head/tail avoid null checks. Layout:
        #   head <-> (MRU) <-> ... <-> (LRU) <-> tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):            # most-recently-used position
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)                 # touch -> move to front
        self._add_front(node)
        return node.val

    def put(self, key, value):
        if key in self.map:
            self._remove(self.map[key])    # will re-add at front with new val
        node = Node(key, value)
        self.map[key] = node
        self._add_front(node)
        if len(self.map) > self.cap:
            lru = self.tail.prev           # node just before tail = LRU
            self._remove(lru)
            del self.map[lru.key]


# ---------- (2) OrderedDict shortcut ----------
class LRUCacheOrdered:
    def __init__(self, capacity):
        self.cap = capacity
        self.od = OrderedDict()            # insertion/most-recent order

    def get(self, key):
        if key not in self.od:
            return -1
        self.od.move_to_end(key)           # mark most-recently-used
        return self.od[key]

    def put(self, key, value):
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)    # pop least-recently-used


def _demo(cls):
    c = cls(2)
    c.put(1, 1); c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)                            # evicts 2
    assert c.get(2) == -1
    c.put(4, 4)                            # evicts 1
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4
    print(f"{cls.__name__}: all assertions passed ✓")


if __name__ == "__main__":
    _demo(LRUCache)
    _demo(LRUCacheOrdered)

# Notes:
# - Map gives O(1) find; the doubly linked list gives O(1) move-to-front and
#   O(1) eviction of the tail. Neither alone is enough.
# - Doubly (not singly) linked: removing an arbitrary node in O(1) needs its
#   predecessor, which only a prev pointer provides.
# - Thread-safety: wrap get/put in a single lock (simplest), or shard the cache
#   to reduce lock contention. Mention the read-vs-write contention tradeoff.

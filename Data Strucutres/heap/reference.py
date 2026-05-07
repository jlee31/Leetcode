# ============================================================
# HEAP / PRIORITY QUEUE
# ============================================================
# When to use:
#   - "kth largest / kth smallest" element
#   - "top k most frequent"
#   - streaming data — need running min/max
#   - merge k sorted lists
#   - always need quick access to the min or max


# ── HEAPQ SYNTAX ────────────────────────────────────────────
# Python's heapq is a MIN HEAP by default

import heapq

heap = []
heapq.heappush(heap, 3)     # push
heapq.heappop(heap)         # pop smallest  O(log n)
heap[0]                     # peek min      O(1) — don't pop
heapq.heapify(nums)         # convert list to heap in-place  O(n)

# Build from list
nums = [3, 1, 4, 1, 5]
heapq.heapify(nums)
heapq.heappop(nums)    # returns 1 (smallest)


# ── MAX HEAP ────────────────────────────────────────────────
# Python has no max heap — negate values to simulate it

heap = []
heapq.heappush(heap, -val)       # push negated
max_val = -heapq.heappop(heap)   # pop and negate back

# Convert list to max heap
nums = [3, 1, 4, 1, 5]
nums = [-x for x in nums]
heapq.heapify(nums)
max_val = -heapq.heappop(nums)


# ── K LARGEST ELEMENTS ──────────────────────────────────────
# Strategy: keep a min heap of size k
# If new element > heap[0] (current smallest), swap it in
# At the end, heap contains the k largest

def k_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)              # O(k)

    for n in nums[k:]:
        if n > heap[0]:
            heapq.heapreplace(heap, n)   # pop min, push n  O(log k)

    return heap   # or heap[0] for kth largest

# Simpler: use nlargest / nsmallest (fine for most problems)
heapq.nlargest(k, nums)             # returns k largest  O(n log k)
heapq.nsmallest(k, nums)            # returns k smallest O(n log k)


# ── TOP K FREQUENT ──────────────────────────────────────────
# Combine Counter + heap

from collections import Counter

def top_k_frequent(nums, k):
    freq = Counter(nums)
    # min heap of size k, keyed by frequency
    return heapq.nlargest(k, freq.keys(), key=lambda x: freq[x])


# ── HEAP WITH TUPLES ────────────────────────────────────────
# Push tuples — heap sorts by first element, then second, etc.
# Use for: k closest points, merge k lists, Dijkstra

heap = []
heapq.heappush(heap, (distance, point))   # sorted by distance
heapq.heappush(heap, (freq, val))         # sorted by freq

# K closest points to origin
def k_closest(points, k):
    heap = []
    for x, y in points:
        dist = x*x + y*y
        heapq.heappush(heap, (dist, x, y))
    return [[x, y] for dist, x, y in heapq.nsmallest(k, heap)]


# ── MERGE K SORTED LISTS ────────────────────────────────────
# Push first element of each list, then keep popping and pushing next

def merge_k_lists(lists):
    dummy = ListNode(0)
    curr = dummy
    heap = []

    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

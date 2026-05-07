# ============================================================
# LINKED LIST
# ============================================================
# When to use:
#   - problem gives you a ListNode
#   - need to reverse, detect cycle, find middle, merge
#   - "in-place" modifications without extra space


# ── NODE DEFINITION ─────────────────────────────────────────

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ── TRAVERSAL ───────────────────────────────────────────────

def traverse(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next


# ── DUMMY NODE ──────────────────────────────────────────────
# Use when you might need to insert/delete at the head
# — avoids edge case handling for empty list or head changes

def use_dummy(head):
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    # ... do work ...
    return dummy.next  # new head


# ── REVERSE LINKED LIST ─────────────────────────────────────
# Must memorize — used constantly as a sub-step

def reverse(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next   # save next
        curr.next = prev  # reverse pointer
        prev = curr       # move prev forward
        curr = nxt        # move curr forward

    return prev  # prev is now the new head


# ── FAST & SLOW POINTERS ────────────────────────────────────
# When to use:
#   - find middle of linked list
#   - detect cycle (Floyd's algorithm)
#   - find start of cycle
#   - find kth node from end

# Find middle (slow stops at middle when fast reaches end)
def find_middle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Detect cycle
def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Find kth node from end (two pointers, k apart)
def kth_from_end(head, k):
    fast = head
    for _ in range(k):          # move fast k steps ahead
        fast = fast.next
    slow = head
    while fast:                 # move both until fast hits end
        slow = slow.next
        fast = fast.next
    return slow                 # slow is now k from end


# ── MERGE TWO SORTED LISTS ──────────────────────────────────

def merge(l1, l2):
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 or l2  # attach remaining
    return dummy.next

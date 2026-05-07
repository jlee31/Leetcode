# ============================================================
# STACK
# ============================================================
# When to use:
#   - "valid parentheses" / matching pairs
#   - undo/redo, browser history
#   - next greater / next smaller element → monotonic stack
#   - DFS iterative implementation
#   - "process in reverse order" — push everything, then pop


# ── STACK SYNTAX (use a list) ───────────────────────────────

stack = []

stack.append(x)    # push  O(1)
stack.pop()        # pop   O(1)  — removes & returns top
stack[-1]          # peek  O(1)  — just look at top, don't remove

if not stack:      # check empty
    pass

len(stack)


# ── VALID PARENTHESES ───────────────────────────────────────
# Classic stack problem — push opens, pop on close

def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()

    return len(stack) == 0


# ── MONOTONIC STACK ─────────────────────────────────────────
# When to use:
#   - "next greater element" to the right or left
#   - "largest rectangle in histogram"
#   - "daily temperatures" (how many days until warmer)
#   - any problem asking about the nearest larger/smaller element
#
# Key idea: maintain a stack that stays sorted (increasing or decreasing)
# by popping elements that violate the order

# Pattern: Next Greater Element (stack stays increasing from bottom)
def next_greater(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices

    for i in range(n):
        # while current num is greater than top of stack → found NGE for top
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result

# Pattern: Daily Temperatures (same idea, store index)
# for each day, how many days until a warmer day?
def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = []  # stores indices

    for i, t in enumerate(temps):
        while stack and t > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)

    return result


# ── MIN STACK ───────────────────────────────────────────────
# Track current minimum at every state
# Trick: store (value, current_min) pairs

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        min_val = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, min_val))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]

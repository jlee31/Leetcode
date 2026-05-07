# ============================================================
# BACKTRACKING
# ============================================================
# When to use:
#   - "find ALL solutions / combinations / subsets / permutations"
#   - explore a decision tree — at each step, make a choice and undo it
#   - brute force with pruning
#
# Mental model:
#   - at each node in the decision tree: CHOOSE → EXPLORE → UNCHOOSE
#   - if a path violates the constraint, prune it (return early)


# ── GENERAL TEMPLATE ────────────────────────────────────────

def backtrack(result, current, start, ...):
    # BASE CASE — found a valid solution
    if is_complete(current):
        result.append(current[:])   # append a COPY, not reference
        return

    for choice in choices_from(start):
        # CHOOSE
        current.append(choice)

        # EXPLORE
        backtrack(result, current, next_start, ...)

        # UNCHOOSE (undo the choice)
        current.pop()


# ── SUBSETS (all 2^n subsets) ───────────────────────────────

def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])   # every state is a valid subset

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)   # i+1 to avoid reuse
            current.pop()

    backtrack(0, [])
    return result


# ── COMBINATIONS (pick k from n) ────────────────────────────

def combine(n, k):
    result = []

    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return

        for i in range(start, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()

    backtrack(1, [])
    return result


# ── COMBINATION SUM (can reuse elements) ────────────────────

def combination_sum(candidates, target):
    result = []

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return   # prune — gone too far

        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])  # i not i+1 → reuse allowed
            current.pop()

    backtrack(0, [], target)
    return result


# ── PERMUTATIONS ────────────────────────────────────────────

def permute(nums):
    result = []

    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])
            return

        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()

    backtrack([], nums)
    return result


# ── WORD SEARCH (backtracking on a grid) ────────────────────
# Same pattern, but "choices" are grid neighbors

def exist(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, i):
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[i]:
            return False

        temp = board[r][c]
        board[r][c] = '#'   # mark visited (CHOOSE)

        found = (backtrack(r+1, c, i+1) or backtrack(r-1, c, i+1) or
                 backtrack(r, c+1, i+1) or backtrack(r, c-1, i+1))

        board[r][c] = temp  # unmark (UNCHOOSE)
        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False

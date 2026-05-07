# ============================================================
# BINARY SEARCH
# ============================================================
# When to use:
#   - sorted array, find a value or boundary
#   - "find minimum/maximum value that satisfies condition" → binary search on answer
#   - rotated sorted array
#   - O(log n) goal instead of O(n)


# ── STANDARD TEMPLATE ───────────────────────────────────────
# Use: find exact value in sorted array

def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:           # ← <= not <
        mid = left + (right - left) // 2   # avoids overflow vs (l+r)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1   # not found


# ── LEFT BOUNDARY ───────────────────────────────────────────
# Use: find first position where condition is True
# e.g. first occurrence of target, or first value >= target

def left_bound(nums, target):
    left, right = 0, len(nums)   # right = len (exclusive)

    while left < right:          # ← strictly <
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid          # shrink right, don't exclude mid yet

    return left   # index of first element >= target


# ── RIGHT BOUNDARY ──────────────────────────────────────────
# Use: find last occurrence of target

def right_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left - 1   # last index of target


# ── ROTATED SORTED ARRAY ────────────────────────────────────
# Key insight: one half is always sorted — figure out which half,
# then decide which side to search

def search_rotated(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1   # target is in left half
            else:
                left = mid + 1    # target is in right half
        # right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1    # target is in right half
            else:
                right = mid - 1   # target is in left half

    return -1


# ── BINARY SEARCH ON ANSWER ─────────────────────────────────
# Use: "find the minimum X such that condition(X) is True"
# The answer space itself is sorted — binary search over possible answers

# Template:
def binary_search_answer(lo, hi):
    # lo = minimum possible answer, hi = maximum possible answer
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):   # define: can we do it with value = mid?
            hi = mid        # try smaller
        else:
            lo = mid + 1    # need bigger
    return lo


# Python built-in binary search (bisect)
import bisect
bisect.bisect_left(nums, target)    # first index where target could go
bisect.bisect_right(nums, target)   # last index where target could go
bisect.insort(nums, target)         # insert and keep sorted

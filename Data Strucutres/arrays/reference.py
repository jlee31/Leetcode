# ============================================================
# ARRAYS
# ============================================================
# When to use:
#   - input is a list/array and you need to search/compare elements
#   - "find a pair", "subarray", "window" → two pointers or sliding window
#   - "running total", "range sum" → prefix sum


# ── PYTHON LIST SYNTAX ──────────────────────────────────────

nums = [1, 2, 3, 4, 5]

nums[0]          # first element
nums[-1]         # last element
nums[1:3]        # slice [2, 3] (end exclusive)
nums[::-1]       # reverse

len(nums)
nums.append(6)
nums.pop()       # removes last
nums.pop(0)      # removes first (slow O(n))

nums.sort()                        # in-place ascending
nums.sort(reverse=True)            # in-place descending
sorted(nums)                       # returns new list
sorted(nums, key=lambda x: x[1])   # sort by second element (for lists of pairs)

min(nums)
max(nums)
sum(nums)

# check if value exists
if 3 in nums:
    pass

# enumerate — gives index + value
for i, val in enumerate(nums):
    pass

# zip — iterate two lists together
for a, b in zip(nums, nums[1:]):
    pass


# ── TWO POINTERS ────────────────────────────────────────────
# When to use:
#   - sorted array, find pair with target sum
#   - palindrome check
#   - "container with most water" type problems
#   - shrink from both ends based on a condition

def two_pointers(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1   # need bigger sum
        else:
            right -= 1  # need smaller sum

    return []

# ── SLIDING WINDOW ──────────────────────────────────────────
# When to use:
#   - "longest/shortest subarray/substring" with some constraint
#   - contiguous elements, no sorting needed
#   - O(n) goal — avoid nested loops

def sliding_window(s):
    seen = set()
    l = 0
    ans = 0

    for r in range(len(s)):
        # SHRINK — kick out s[l] while window is invalid
        while s[r] in seen:
            seen.remove(s[l])
            l += 1

        # EXPAND — add s[r]
        seen.add(s[r])

        # UPDATE answer
        ans = max(ans, r - l + 1)

    return ans

# fixed-size window (size k):
def fixed_window(nums, k):
    window_sum = sum(nums[:k])
    ans = window_sum

    for r in range(k, len(nums)):
        window_sum += nums[r] - nums[r - k]  # slide: add right, remove left
        ans = max(ans, window_sum)

    return ans


# ── PREFIX SUM ──────────────────────────────────────────────
# When to use:
#   - range sum queries (sum from index i to j)
#   - "subarray sum equals k" → use prefix + hashmap

def build_prefix(nums):
    prefix = [0] * (len(nums) + 1)
    for i, val in enumerate(nums):
        prefix[i + 1] = prefix[i] + val
    return prefix

# sum from i to j (inclusive) = prefix[j+1] - prefix[i]

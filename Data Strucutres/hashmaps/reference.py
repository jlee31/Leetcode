# ============================================================
# HASHMAPS & SETS
# ============================================================
# When to use:
#   - O(1) lookup — "have I seen this before?"
#   - frequency counting — "how many times does X appear?"
#   - grouping — "group anagrams", "group by key"
#   - two sum type — "does target - x exist?"


# ── DICT SYNTAX ─────────────────────────────────────────────

seen = {}

seen[key] = value          # add / update
seen[key]                  # get (KeyError if missing)
seen.get(key, 0)           # get with default (safe)
del seen[key]              # delete

if key in seen:            # check existence
    pass

for key, val in seen.items():   # iterate key+value
    pass
for key in seen:                # just keys
    pass
for val in seen.values():       # just values
    pass


# ── DEFAULTDICT ─────────────────────────────────────────────
# Use when you're building up a dict (counting, grouping)
# — avoids checking "if key not in dict" every time

from collections import defaultdict

count = defaultdict(int)    # default value: 0
count[key] += 1             # no KeyError

groups = defaultdict(list)  # default value: []
groups[key].append(val)


# ── COUNTER ─────────────────────────────────────────────────
# Fastest way to count frequencies

from collections import Counter

freq = Counter(nums)        # {element: count}
freq = Counter(s)           # works on strings too

freq.most_common(k)         # top k most frequent as [(val, count), ...]
freq[x]                     # count of x (returns 0 if missing)


# ── SET SYNTAX ──────────────────────────────────────────────
# Use when you only need existence checks, not values

seen = set()
seen.add(x)
seen.remove(x)      # KeyError if missing
seen.discard(x)     # safe remove

if x in seen:
    pass

a & b   # intersection
a | b   # union
a - b   # difference


# ── PATTERNS ────────────────────────────────────────────────

# Pattern 1: Two Sum (seen + complement)
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []

# Pattern 2: Group Anagrams (sorted string as key)
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())

# Pattern 3: Frequency comparison (check if two strings are anagrams)
def is_anagram(s, t):
    return Counter(s) == Counter(t)

# Pattern 4: Sliding window with freq count (at most k distinct chars)
def at_most_k_distinct(s, k):
    freq = defaultdict(int)
    l = 0
    ans = 0
    for r in range(len(s)):
        freq[s[r]] += 1
        while len(freq) > k:
            freq[s[l]] -= 1
            if freq[s[l]] == 0:
                del freq[s[l]]
            l += 1
        ans = max(ans, r - l + 1)
    return ans

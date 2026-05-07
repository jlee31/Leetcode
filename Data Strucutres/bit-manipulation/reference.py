# ============================================================
# BIT MANIPULATION
# ============================================================
# When to use:
#   - problem involves binary representation
#   - "single number" (XOR trick)
#   - "count 1 bits" / "power of two" checks
#   - O(1) space tricks that would otherwise need a set/map


# ── PYTHON BIT OPERATORS ────────────────────────────────────

a & b    # AND  — both bits are 1
a | b    # OR   — at least one bit is 1
a ^ b    # XOR  — exactly one bit is 1 (different)
~a       # NOT  — flip all bits
a << n   # left shift  — multiply by 2^n
a >> n   # right shift — divide by 2^n (floor)


# ── COMMON TRICKS ───────────────────────────────────────────

# Check if bit i is set
(n >> i) & 1

# Set bit i
n | (1 << i)

# Clear bit i
n & ~(1 << i)

# Check if n is a power of 2  (only one bit set)
n > 0 and (n & (n - 1)) == 0

# Get lowest set bit
n & (-n)

# Remove lowest set bit (Brian Kernighan's trick — used to count 1s)
n & (n - 1)

# Count number of 1 bits
def count_bits(n):
    count = 0
    while n:
        n &= (n - 1)   # remove lowest set bit each time
        count += 1
    return count

# Python built-in
bin(n).count('1')
n.bit_count()          # Python 3.10+


# ── XOR PROPERTIES ──────────────────────────────────────────
# a ^ a = 0         (a number XORed with itself = 0)
# a ^ 0 = a         (a number XORed with 0 = itself)
# XOR is commutative and associative

# Single Number — find the one element that appears once
# (all others appear twice)
def single_number(nums):
    res = 0
    for n in nums:
        res ^= n   # pairs cancel out, single number remains
    return res

# Sum of two integers without + operator
def get_sum(a, b):
    mask = 0xFFFFFFFF   # 32-bit mask
    while b & mask:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return a if b == 0 else a & mask   # handle negative numbers


# ── COMMON PATTERNS ─────────────────────────────────────────

# Reverse bits (32-bit unsigned integer)
def reverse_bits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

# Missing number (0 to n, one missing)
# XOR all indices with all values — pairs cancel, missing remains
def missing_number(nums):
    res = len(nums)
    for i, n in enumerate(nums):
        res ^= i ^ n
    return res

# Count bits for 0..n (DP approach)
def count_bits_dp(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)   # dp[i] = dp[i//2] + last bit
    return dp


# ── BIT MASKS FOR SUBSETS ───────────────────────────────────
# Enumerate all subsets of n elements using bitmask

def all_subsets(nums):
    n = len(nums)
    result = []
    for mask in range(1 << n):   # 2^n subsets
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        result.append(subset)
    return result

# ============================================================
# DYNAMIC PROGRAMMING
# ============================================================
# When to use:
#   - "how many ways", "maximum/minimum value", "is it possible"
#   - overlapping subproblems — same sub-question computed multiple times
#   - optimal substructure — answer to big problem = function of smaller problems
#
# Approach:
#   1. Define what dp[i] means in plain English
#   2. Find the recurrence (how does dp[i] relate to dp[i-1], dp[i-2], etc.)
#   3. Set base cases
#   4. Fill the table


# ── 1D DP ───────────────────────────────────────────────────

# Climbing Stairs (how many ways to reach step n using 1 or 2 steps)
# dp[i] = number of ways to reach step i
# dp[i] = dp[i-1] + dp[i-2]  (came from i-1 or i-2)
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Optimized (only need last 2 values — O(1) space)
def climb_stairs_opt(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

# House Robber (can't rob adjacent houses)
# dp[i] = max money robbing houses 0..i
# dp[i] = max(dp[i-1], dp[i-2] + nums[i])
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[-1]

# Coin Change (fewest coins to make amount)
# dp[i] = min coins to make amount i
# dp[i] = min(dp[i - coin] + 1) for each coin
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0   # base case: 0 coins to make amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Longest Increasing Subsequence
# dp[i] = length of LIS ending at index i
# dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]
def length_of_lis(nums):
    dp = [1] * len(nums)   # every element is LIS of length 1 by itself
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# ── 2D DP ───────────────────────────────────────────────────

# Unique Paths (m x n grid, move only right or down)
# dp[r][c] = number of paths to reach cell (r, c)
# dp[r][c] = dp[r-1][c] + dp[r][c-1]
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]   # base: top row and left col = 1

    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]

    return dp[m-1][n-1]

# Longest Common Subsequence
# dp[i][j] = LCS of s1[:i] and s2[:j]
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1   # extend match
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])   # skip one char

    return dp[m][n]

# 0/1 Knapsack
# dp[i][w] = max value using first i items with capacity w
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]   # don't take item i
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])

    return dp[n][capacity]


# ── MEMOIZATION (top-down) ──────────────────────────────────
# Alternative to bottom-up — use recursion + cache

from functools import lru_cache

def climb_stairs_memo(n):
    @lru_cache(maxsize=None)
    def dp(i):
        if i <= 1:
            return 1
        return dp(i-1) + dp(i-2)
    return dp(n)

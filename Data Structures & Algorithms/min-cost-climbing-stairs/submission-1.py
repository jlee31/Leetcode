class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [n+1] * n
        i = 0
        curr = 0
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])
        #dp[i]=cost[i]+min(dp[i−1],dp[i−2])
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,n):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[n-1], dp[n-2])
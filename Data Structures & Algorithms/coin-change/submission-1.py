class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        maxNum = amount+1
        dp = [maxNum] * maxNum
        dp[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if (i - coin) >= 0 and dp[i-coin] <= amount:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        if dp[amount] == maxNum: # still no solution?
            dp[amount] = -1
        
        return dp[amount]
        

 
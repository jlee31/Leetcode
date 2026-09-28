class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] < prices[r]:
                curr_profit = prices[r] - prices[l]
                best_profit = max(best_profit, curr_profit)
            else:
                l = r
            r += 1
        return best_profit
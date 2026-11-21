class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp solution
        n = len(nums)
        max_dp = [0] * n
        min_dp = [0] * n

        max_dp[0] = nums[0]
        min_dp[0] = nums[0]

        ret = nums[0]

        for i in range(1,n):
            v = nums[i]
            max_dp[i] = max(v, min_dp[i-1] * v, max_dp[i-1] * v)
            min_dp[i] = min(v, min_dp[i-1] * v, max_dp[i-1] * v)
            
            ret = max(ret, max_dp[i])

        return ret


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        best = curr = nums[0]
        for i in range(1,n):
            curr = max(nums[i], curr + nums[i])
            best = max(best, curr)
        return best
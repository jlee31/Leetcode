class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(len(nums) + 1):
            result ^= i          # XOR with expected range
            if i < len(nums):
                result ^= nums[i]  # XOR with actual array
        
        return result
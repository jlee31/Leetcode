class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for idx, num in enumerate(nums):
            if target - num in seen:
                return [idx, seen[target - num]]
            else:
                seen[num] = idx

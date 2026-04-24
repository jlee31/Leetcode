class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        count = 0
        for i in range(l):
            if nums[i] == target:
                return count
            count += 1
        return -1
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False
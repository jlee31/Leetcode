class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        s = set()
        for num in nums:
            if num in s:
                return num
            else:
                s.add(num)
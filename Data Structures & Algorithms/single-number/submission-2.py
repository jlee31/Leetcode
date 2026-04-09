class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ok only O(1) extra space and o(n) so i cant sort
        ret = nums[0]
        n = len(nums)
        for i in range(1, n):
            ret = ret ^ nums[i]
        return ret


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0] * n * 2
        for i in range(n):
            ret[i] = nums[i]
            ret[i + n] = nums[i]
        return ret
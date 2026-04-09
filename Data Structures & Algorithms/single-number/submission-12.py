from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = reduce(lambda x, y: x^y, nums, 0)
        return ans
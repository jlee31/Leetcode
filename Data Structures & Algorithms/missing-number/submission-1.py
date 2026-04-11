class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # first an o(n) Solution
        n = len(nums)
        s = set()
        for num in nums:
            s.add(num)
        for i in range(1,n+1):
            if i not in s:
                return i
        return 0

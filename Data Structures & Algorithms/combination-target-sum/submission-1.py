class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        curr = []
        n = len(nums)

        def backtrack(i, currSum):
            if currSum == target:
                ret.append(curr[:]) # a copy of the current
                return
            
            if currSum > target or i == n:
                return
            
            backtrack(i+1, currSum)
            
            curr.append(nums[i])
            backtrack(i, currSum+nums[i])
            curr.pop()

        backtrack(0,0)
        return ret
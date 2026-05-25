class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        def backtrack(index, path):
            if index == len(nums):
                ret.append(path[:])
                return
            
            path.append(nums[index])
            backtrack(index+1, path)
            
            path.pop()
            backtrack(index+1, path)

        backtrack(0,[])
        return ret
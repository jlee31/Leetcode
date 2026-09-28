class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = []
        n = len(nums)
        
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[r] + nums[l]
                if s == 0:
                    if [nums[i], nums[r], nums[l]] not in ret:
                        ret.append([nums[i], nums[r], nums[l]])
                    l += 1
                if s > 0:
                    r -= 1
                if s < 0:
                    l += 1
        return ret
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp_1 = [0] * (n-1)
        dp_2 = [0] * (n-1)

        dp_1[0] = nums[0]
        for i in range(1, n-1):
            dp_1[i] = max(dp_1[i-1], dp_1[i-2] + nums[i])

        dp_2[0] = nums[1]
        for i in range(1, n-1):
            dp_2[i] = max(dp_2[i-1], (dp_2[i-2] if i >= 2 else 0) + nums[i+1])
        
        print(dp_1)
        print(dp_2)

        return max(dp_1[n-2], dp_2[n-2])
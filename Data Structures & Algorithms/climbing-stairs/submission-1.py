class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        ret = [0] * n
        ret[0] = 1
        ret[1] = 2

        for i in range(2,n):
            ret[i] = ret[i-1] + ret[i-2]
        
        return ret[-1]
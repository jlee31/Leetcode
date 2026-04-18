class Solution:
    def myPow(self, x: float, n: int) -> float:
        runningPower = 1
        val = x
        if n == 0:
            return 1
        if n < 0:
            for i in range((-1*n) + 1):
                x *= 1 / val
        else:
            for i in range(n-1):
                x *= val
        return x
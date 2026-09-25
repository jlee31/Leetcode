class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)

        for i, val in enumerate(temperatures):
            while stk and val > temperatures[stk[-1]]: # while the value is greater than the top of the stack
                idx = stk.pop()
                res[idx] = i - idx
            stk.append(i)
        return res
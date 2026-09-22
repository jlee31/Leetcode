# proper
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ret = [0] * len(temperatures)

        for ind, temp in enumerate(temperatures):
            while stk and temp > temperatures[stk[-1]]:
                prev_i = stk.pop()
                distance = ind - prev_i
                ret[prev_i] = distance
            stk.append(ind)
        return ret

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        count = 0
        times = []
        for idx, pos in enumerate(position):
            time = (target - pos) / speed[idx]
            times.append([pos,time])
        times.sort(reverse=True)
        for pos, time in times:
            if not stk or stk[-1] < time:
                stk.append(time)
                count += 1
        return count
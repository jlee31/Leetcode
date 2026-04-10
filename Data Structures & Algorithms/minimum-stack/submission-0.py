class MinStack:

    def __init__(self):
        self.s = []
        self.len = 0

    def push(self, val: int) -> None:
        self.s.append(val)
        self.len += 1

    def pop(self) -> None:
        self.s.pop()
        self.len -= 1

    def top(self) -> int:
        if self.len > 0:
            return self.s[-1]
        else:
            return 0
        
    def getMin(self) -> int:
        min_v = float('inf')
        for num in self.s:
            if num <= min_v:
                min_v = num
        return min_v
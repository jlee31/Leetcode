class MinStack:

    def __init__(self):
        self.s = []
        self.min_s = [] 

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.min_s:
            self.min_s.append(min(val, self.min_s[-1]))
        else:
            self.min_s.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.min_s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_s[-1]  # O(1) ✅
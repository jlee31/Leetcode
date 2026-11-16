
class TimeMap:

    def __init__(self):
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = []

        self.values[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""

        arr = self.values[key]
        left = 0
        right = len(arr) - 1
        ret = ""

        while left <= right:
            mid = (left + right) // 2

            if arr[mid][0] <= timestamp:
                ret = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return ret
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-x for x in nums]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        tmp = self.nums[:]
        tmp_val = 0
        for i in range(self.k):
            tmp_val = heapq.heappop(tmp)
        return -1 * tmp_val

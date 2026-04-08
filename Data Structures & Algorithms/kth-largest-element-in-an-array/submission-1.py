import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] *= -1
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)
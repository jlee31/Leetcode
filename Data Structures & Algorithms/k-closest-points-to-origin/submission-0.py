import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        distances = [0] * n # index in list, distance
        for i, point in enumerate(points):
            distances[i] = [math.sqrt((0 - point[0]) ** 2 + (0 - point[1]) ** 2), i]
        heapq.heapify(distances)
        ret = [0] * k
        for i in range(k):
            ret[i] = heapq.heappop(distances) # the index
        for i in range(k):
            ret[i] = ret[i] = points[ret[i][1]]
        return ret
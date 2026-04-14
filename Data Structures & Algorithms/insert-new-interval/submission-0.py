class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # first insert it then do a merge afterwards
        l = len(intervals)
        i = 0 # to count the index
        ret = []

        # add all intervals before newInterval

        while i < l and intervals[i][1] < newInterval[0]:
            ret.append(intervals[i])
            i += 1

        # merge all overlapping into nerInterval
        while i < l and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        ret.append(newInterval)

        # add any intervals that are afterwards
        while i < l:
            ret.append(intervals[i])
            i += 1

        return ret
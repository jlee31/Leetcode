"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        l = len(intervals)
        # seperate into two 
        start = [0] * l
        end = [0] * l
        
        for i in range(l):
            start[i] = intervals[i].start
            end[i] = intervals[i].end

        start.sort()
        end.sort()

        #
        numRooms = 0
        j = 0
        for i in range(l):
            if start[i] >= end[j]:
                j += 1
            else:
                numRooms += 1


        return numRooms

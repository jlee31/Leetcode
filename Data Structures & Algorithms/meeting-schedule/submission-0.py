"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda i: i.start)
        n = len(intervals)
        for i in range(1, n):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True
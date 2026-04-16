class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        l = len(intervals)
        intervals.sort(key=lambda x:x[1])
        
        print(intervals)

        count = 0
        prev_end = intervals[0][1]

        for i in range(1, l):
            if intervals[i][0] < prev_end:
                count += 1
            else:
                prev_end = intervals[i][1]

        return count 
        

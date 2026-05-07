# ============================================================
# INTERVALS
# ============================================================
# When to use:
#   - input is a list of [start, end] pairs
#   - "merge overlapping", "remove overlapping", "insert interval"
#   - meeting rooms, schedule conflicts
#
# Golden rule: SORT BY START TIME first (almost always)


# ── OVERLAP CHECK ───────────────────────────────────────────
# Two intervals [a, b] and [c, d] overlap if: a < d AND c < b
# (i.e. one starts before the other ends)

def overlaps(a, b):
    return a[0] < b[1] and b[0] < a[1]


# ── MERGE INTERVALS ─────────────────────────────────────────
# Sort by start, then greedily merge

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= result[-1][1]:           # overlaps with last merged
            result[-1][1] = max(result[-1][1], end)   # extend end
        else:
            result.append([start, end])      # no overlap, add new

    return result


# ── INSERT INTERVAL ─────────────────────────────────────────
# Insert a new interval into a sorted, non-overlapping list

def insert(intervals, new):
    result = []
    i = 0
    n = len(intervals)

    # 1. Add all intervals that end before new starts (no overlap)
    while i < n and intervals[i][1] < new[0]:
        result.append(intervals[i])
        i += 1

    # 2. Merge all overlapping intervals
    while i < n and intervals[i][0] <= new[1]:
        new[0] = min(new[0], intervals[i][0])
        new[1] = max(new[1], intervals[i][1])
        i += 1
    result.append(new)

    # 3. Add remaining
    result.extend(intervals[i:])
    return result


# ── NON-OVERLAPPING INTERVALS ───────────────────────────────
# Minimum removals to make all intervals non-overlapping
# Greedy: sort by END time, keep interval with earliest end
# (classic "activity selection" greedy)

def erase_overlap(intervals):
    intervals.sort(key=lambda x: x[1])   # sort by END
    count = 0
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start < prev_end:    # overlap — remove current
            count += 1
        else:
            prev_end = end      # no overlap — keep, update boundary

    return count


# ── MEETING ROOMS I ─────────────────────────────────────────
# Can one person attend all meetings? → any overlap = False

def can_attend_all(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True


# ── MEETING ROOMS II ────────────────────────────────────────
# Minimum number of rooms needed
# Strategy: use a min heap of end times — if next meeting starts
# after earliest ending meeting, reuse that room

import heapq

def min_rooms(intervals):
    intervals.sort(key=lambda x: x[0])
    heap = []   # stores end times of ongoing meetings

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)   # reuse room
        else:
            heapq.heappush(heap, end)      # need new room

    return len(heap)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # iterate through the intervals
        # we detect an overlap if the current interval start time is less than the last interval end time.
        # if we detect an overlap, we increment the answer count.
        # then we remove one of the intervals.
        # which one do we remove?
        # we remove the one with the later end time so we can avoid overlaps
        # so we set the previous interval (target of comparison)'s end to the smaller one
        prev = 0
        i = 1
        answer = 0
        while i < len(intervals):
            if intervals[i][0] < intervals[prev][1]:
                # overlap
                answer += 1
                intervals[prev][1] = min(intervals[prev][1], intervals[i][1])
            else:
                # no overlap, set previous interval to current interval
                prev = i
            i += 1
        return answer
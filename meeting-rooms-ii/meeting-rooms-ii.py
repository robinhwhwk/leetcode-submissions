class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # if two intervals are overlapping, then we need 2 rooms
        # find the max number of intervals that overlap at any given time
        # check every time period from [min(intervals[0]), max(intervals[1])] inclusive
        min_start = float('inf')
        max_end = 0
        for interval in intervals:
            min_start = min(interval[0], min_start)
            max_end = max(interval[1], max_end)

        max_count = 0
        for interval in intervals:
            t = interval[0]
            count = 0
            for interval in intervals:
                if interval[0] <= t and interval[1] > t:
                    count += 1
            max_count = max(max_count, count)
        return max_count



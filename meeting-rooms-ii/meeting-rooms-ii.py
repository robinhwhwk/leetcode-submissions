class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort the intervals by start time
        times = []
        for interval in intervals:
            times.append([interval[0], 1])
            times.append([interval[1], -1])
        times.sort()
        res = 0
        curr = 0
        for i in range(len(times)):
            curr += times[i][1]
            res = max(res, curr)
        return res

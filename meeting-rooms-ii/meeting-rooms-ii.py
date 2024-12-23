class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # intuition: find the maximum number of overlapping intervals
        events = [] # store tuples of (time, event_type)
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, 0))
        maxEvents = 0
        currEvents = 0
        events.sort()
        for time, event in events:
            if event == 1:
                currEvents += 1
            else:
                currEvents -= 1
            maxEvents = max(maxEvents, currEvents)
        return maxEvents

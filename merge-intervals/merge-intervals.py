class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # sort by end
        stack = []
        for interval in intervals:
            if stack and stack[-1][1] >= interval[0]:
                newEnd = max(stack[-1][1], interval[1])
                stack[-1][1] = newEnd
            else:
                stack.append(interval)
        return stack
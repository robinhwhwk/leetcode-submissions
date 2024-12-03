class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # sort by end
        stack = []
        for interval in intervals:
            while stack and stack[-1][1] >= interval[0]:
                newEnd = max(stack[-1][1], interval[1])
                interval = [stack[-1][0], newEnd]
                stack.pop()
            stack.append(interval)
        return stack
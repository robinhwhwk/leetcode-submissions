class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # keep a stack of tuples: (temperature, index)
        # once we encounter a new temp, pop all from stack with temp < curr
        # when we pop, set arr[index] = currIndex - index
        stack = [0 for _ in range(len(temperatures))]
        res = [0 for _ in range(len(temperatures))]
        top = -1
        for i in range(len(temperatures)):
            current_temp = temperatures[i]
            while top != -1 and current_temp > temperatures[stack[top]]:
                res[stack[top]] = i - stack[top]
                top -= 1
            top += 1
            stack[top] = i
        return res

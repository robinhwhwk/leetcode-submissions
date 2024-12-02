class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # keep a stack of tuples: (temperature, index)
        # once we encounter a new temp, pop all from stack with temp < curr
        # when we pop, set arr[index] = currIndex - index
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            current_temp = temperatures[i]
            while stack and current_temp > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append([current_temp, i])
        return res

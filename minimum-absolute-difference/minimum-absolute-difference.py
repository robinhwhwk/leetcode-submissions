class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # keep min abs difference as we iterate
        # if we see a match, store it somewhere
        # if min abs is lower, update and reset the store
        min_diff = float('inf')
        arr.sort()
        res = []
        for i in range(1, len(arr)):
            num1, num2 = arr[i-1], arr[i]
            if abs(num2 - num1) < min_diff:
                min_diff = abs(num2 - num1)
                res = [[num1, num2]]
            elif abs(num2 - num1) == min_diff:
                res.append([num1, num2])
        return res
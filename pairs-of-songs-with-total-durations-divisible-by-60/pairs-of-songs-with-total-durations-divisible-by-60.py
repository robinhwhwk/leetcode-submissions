class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        complements = dict() # stores complement % 60
        result = 0
        for num in time:
            num = num % 60
            if (60 - num) % 60 in complements:
                result += complements[(60 - num) % 60]
            if num not in complements:
                complements[num] = 0
            complements[num] += 1
        return result


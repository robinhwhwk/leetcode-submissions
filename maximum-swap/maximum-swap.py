class Solution:
    def maximumSwap(self, num: int) -> int:
        # find the first digit that is bigger than a digit before it
        maxIndex = 0
        swapIndex = (0, 0)
        maxDigit = 0
        string_num = str(num)
        for i in range(len(string_num)-1, -1, -1):
            digit = int(string_num[i])
            if maxDigit > digit and i < maxIndex:
                swapIndex = i, maxIndex
            elif digit > maxDigit:
                maxDigit = digit
                maxIndex = i
        string_num = list(string_num)
        string_num[swapIndex[0]], string_num[swapIndex[1]] = string_num[swapIndex[1]], string_num[swapIndex[0]]
        return int("".join(string_num))

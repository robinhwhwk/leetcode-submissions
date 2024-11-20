class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # empty list for each row
        result = [[] for _ in range(numRows)]
        index = 0
        direction = 1
        for i in range(len(s)):
            ch = s[i]
            result[index].append(ch)
            if index == numRows - 1:
                direction = -1
            elif index == 0:
                direction = 1
            index += direction
            index %= numRows
        res = ""
        for l in result:
            res += "".join(l)
        return res

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ["" for _ in range(len(spaces) + len(s))]
        index = 0
        for i in range(len(s)):
            if index < len(spaces) and i == spaces[index]:
                res[i + index] = " "
                index += 1
            res[i + index] = s[i]
        return "".join(res)
            
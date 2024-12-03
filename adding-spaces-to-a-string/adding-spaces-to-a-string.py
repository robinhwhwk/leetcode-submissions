class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        index = 0
        for i in range(len(s)):
            if index < len(spaces) and i == spaces[index]:
                index += 1
                res += " "
            res += s[i]
        return res
            
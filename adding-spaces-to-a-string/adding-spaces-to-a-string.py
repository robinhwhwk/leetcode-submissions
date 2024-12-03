class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        for i in range(len(s)):
            if spaces and i == spaces[0]:
                spaces.pop(0)
                res += " "
            res += s[i]
        return res
            
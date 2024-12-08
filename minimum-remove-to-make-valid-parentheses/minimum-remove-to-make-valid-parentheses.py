class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # iterate through the string
        # if you see backwards without forward parentheses in stack:
        #   remove backwards
        # if you see forward:
        #   add to stack
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append((i,"("))
            elif s[i] == ")":
                if stack and stack[-1][1] == "(":
                    stack.pop(-1)
                else:
                    stack.append((i, ")"))
        res = ""
        for j in range(len(s)):
            if stack and j == stack[0][0]:
                stack.pop(0)
            else:
                res += s[j]
        return res
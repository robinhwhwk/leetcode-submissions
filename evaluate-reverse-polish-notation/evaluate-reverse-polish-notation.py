class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1 + op2)
            elif token == "-":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 - op1)
            elif token == "*":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1 * op2)
            elif token == "/":
                op1 = stack.pop()
                op2 = stack.pop()
                res = op2 / op1
                res = int(res)
                stack.append(res)
            else: # token is integer
                stack.append(int(token))
            # print(stack)
        return stack.pop()

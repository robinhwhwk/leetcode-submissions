class Solution:
    def decodeString(self, s: str) -> str:
        current_string = ""
        current_num = 0
        stack = []
        for ch in s:
            if ch == "[":
                stack.append(current_string)
                stack.append(current_num)
                current_string = ""
                current_num = 0
            elif ch == "]":
                last_num = stack.pop()
                last_string = stack.pop()
                current_string = last_string + last_num * current_string
            elif ch.isdigit():
                current_num = current_num * 10 + int(ch)
            else:
                current_string += ch
        return current_string
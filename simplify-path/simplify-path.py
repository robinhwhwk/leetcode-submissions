class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split("/")
        stack = []
        for d in directories:
            if not d:
                continue
            if d == "..":
                if stack:
                    stack.pop(-1)
            elif d != ".":
                stack.append(d)
        return "/" + "/".join([d for d in stack if d])
        
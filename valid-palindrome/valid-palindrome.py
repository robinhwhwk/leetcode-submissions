class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = set("abcdefghijklmnopqrstuvwxyz0123456789")
        start, end = 0, len(s) - 1
        s = s.lower()
        while start < end:

            if s[start] == s[end]:
                start += 1
                end -= 1
            elif s[start] not in alphanumeric:
                start += 1
            elif s[end] not in alphanumeric:
                end -= 1
            else:
                return False
        return True
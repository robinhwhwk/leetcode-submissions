class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            start, end = 0, len(s) - 1
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True
        
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return isPalindrome(s[start:end]) or isPalindrome(s[start+1:end+1])
        return True
            
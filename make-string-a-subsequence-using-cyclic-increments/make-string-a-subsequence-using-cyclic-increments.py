class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def isSubsequence(str1, str2, m, n):
            # base case
            if n == 0:
                return True
            elif m == 0:
                return False
            modified_char = chr(ord(str1[m-1]) + 1) if str1[m-1] != 'z' else 'a'
            if str1[m - 1] == str2[n - 1] or modified_char == str2[n-1]:
                return isSubsequence(str1, str2, m - 1, n - 1)
            else:
                return isSubsequence(str1, str2, m - 1, n)
        return isSubsequence(str1, str2, len(str1), len(str2))
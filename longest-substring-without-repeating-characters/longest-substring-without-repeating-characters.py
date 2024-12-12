class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_occurrence = dict()
        start = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] in last_occurrence:
                start = max(start, last_occurrence[s[i]] + 1)
                last_occurrence[s[i]] = i
            last_occurrence[s[i]] = i
            max_len = max(max_len, i - start + 1)
        return max_len
                
            
            

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_occurence = dict()
        longest_length = 0
        start = 0
        for end in range(len(s)):
            if s[end] in last_occurence:
                start = max(start, last_occurence[s[end]] + 1)
            last_occurence[s[end]] = end
            longest_length = max(longest_length, end - start + 1)

            last_occurence[s[end]] = end
        return longest_length

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep last occurence for each character
        # increment if current character is not in last occurence
        # if current character is in last occurence:
        #   move start pointer to 1 + last encountered[char]
        last_occurence = dict()
        start = end = max_len = 0
        current_len = 0
        for end in range(len(s)):
            if s[end] in last_occurence:
                start = max(last_occurence[s[end]] + 1, start)
            current_len = end - start + 1
            max_len = max(max_len, current_len)
            last_occurence[s[end]] = end
        return max_len





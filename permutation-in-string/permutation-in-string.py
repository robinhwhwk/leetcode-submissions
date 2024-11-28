class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        left, right = 0, len(s1) - 1
        while right < len(s2) - 1:
            # check the substring from [left, right] inclusive
            if s1_count == s2_count:
                return True
            s2_count[ord(s2[left]) - ord('a')] -= 1
            left += 1
            right += 1
            s2_count[ord(s2[right]) - ord('a')] += 1
            if s1_count == s2_count:
                return True
        return False
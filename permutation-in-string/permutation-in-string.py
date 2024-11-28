class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        alphabet_count = [0 for _ in range(26)]
        for ch in s1:
            alphabet_count[ord(ch) - ord('a')] += 1
        left = 0
        for right in range(len(s2)):
            # subtract 1 from s2[right]
            alphabet_count[ord(s2[right]) - ord('a')] -= 1
            # move left up until substring doesn't contain more chars than needed 
            while left < right and min(alphabet_count) < 0:
                alphabet_count[ord(s2[left]) - ord('a')] += 1
                left += 1
            if not any(alphabet_count):
                return True
            

        return False
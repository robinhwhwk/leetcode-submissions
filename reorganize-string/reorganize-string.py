class Solution:
    def reorganizeString(self, s: str) -> str:
        count = dict()
        max_count = 0
        max_char = ""
        for ch in s:
            if ch not in count:
                count[ch] = 0
            count[ch] += 1
            if count[ch] > max_count:
                max_count = count[ch]
                max_char = ch
        if 2 * max_count > len(s) + 1:
            return ""
        res = ["" for _ in range(len(s))]
        index = 0
        count[max_char] = 0
        for i in range(max_count):
            res[index] = max_char
            index += 2
        for ch in count:
            while count[ch] > 0:
                count[ch] -= 1
                if index >= len(s):
                    index = 1
                res[index] = ch
                index += 2
        return "".join(res)
        
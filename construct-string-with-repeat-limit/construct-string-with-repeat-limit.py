class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # get count of all alphabets
        count = dict()
        for ch in s:
            if ch not in count:
                count[ch] = 0
            count[ch] += 1
        heap = [(-ord(ch), freq) for ch, freq in count.items()]
        heapq.heapify(heap)
        res = ""
        while heap:
            current_ord, freq = heapq.heappop(heap)
            current_char = chr(-1 * current_ord)
            if freq <= repeatLimit:
                res += current_char * freq
            else:
                res += current_char * repeatLimit
                if not heap:
                    return res
                second_ord, second_freq = heapq.heappop(heap)
                second_char = chr(-1 * second_ord)
                res += second_char
                if second_freq > 1:
                    heapq.heappush(heap, (second_ord, second_freq-1))
                heapq.heappush(heap, (current_ord, freq - repeatLimit))
        return res
        


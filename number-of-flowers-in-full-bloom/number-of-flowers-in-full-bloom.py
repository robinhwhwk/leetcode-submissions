class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        events = []
        for flower in flowers:
            events.append((flower[0], 1))
            events.append((flower[1] + 1, -1))
        for i in range(len(people)):
            events.append((people[i], 2, i))
        events.sort()
        res = [0 for _ in range(len(people))]
        count = 0
        for event in events:
            if event[1] != 2:
                count += event[1]
            else:
                res[event[2]] = count
        return res

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        events = []
        for i in range(len(username)):
            user = username[i]
            site = website[i]
            t = timestamp[i]
            heapq.heappush(events, (t, site, user))
        
        users = dict()
        while events:
            t, site, user = heapq.heappop(events)
            if user not in users:
                users[user] = []
            users[user].append(site)

        # process resulting arrays
        patterns = dict()
        for user in users:
            sites = users[user]
            user_patterns = set()
            for i in range(len(sites) - 2):
                for j in range(i + 1, len(sites) - 1):
                    for k in range(j + 1, len(sites)):
                        pattern = ",".join([sites[i], sites[j], sites[k]])
                        if pattern in user_patterns:
                            continue
                        if pattern not in patterns:
                            patterns[pattern] = 0
                        patterns[pattern] += 1
                        user_patterns.add(pattern)
        max_heap = [(-count, pattern) for pattern, count in patterns.items()]
        heapq.heapify(max_heap)
        result = heapq.heappop(max_heap)
        return result[1].split(",")

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = dict()
        for task in tasks:
            if task not in count:
                count[task] = 0
            count[task] += 1
        priority_queue = []
        for task in count:
            heapq.heappush(priority_queue, (-1 * count[task], task))
        time = 0
        while priority_queue:
            removed_list = []
            for i in range(n + 1):
                time += 1
                if not priority_queue:
                    continue
                prio, task = heapq.heappop(priority_queue)
                if prio < -1:
                    removed_list.append((prio + 1, task))
                if not removed_list and not priority_queue:
                    return time
            for i in range(len(removed_list)):
                heapq.heappush(priority_queue, removed_list[i])
        return time
                
                
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = dict()
        for task in tasks:
            if task not in count:
                count[task] = 0 
            count[task] += 1
        # A: 3, B: 3
        priority_queue = [[-freq, task] for (task, freq) in count.items()]
        heapq.heapify(priority_queue) # O(n)
        time = 0
        while priority_queue:
            removed_tasks = []
            for i in range(n + 1):
                if priority_queue:
                    freq, task = heapq.heappop(priority_queue)
                    if freq < -1:
                        removed_tasks.append([freq + 1, task])
                    time += 1
                elif removed_tasks:
                    time += 1
                else:
                    return time
            for removed_task in removed_tasks:
                heapq.heappush(priority_queue, removed_task)
        return time
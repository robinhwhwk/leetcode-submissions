class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # keep track of the number of tasks left for each label
        # ex) A: 3, B: 3
        # pull the task with the highest # of tasks left at each time step
        # for each time in interval (n + 1):
        #   pull the highest prio task from heap
        #   add it to the list of pulled tasks with prio - 1
        # add back the pulled tasks into heap
        items = dict() # indicate the priority of each task
        for task in tasks:
            if task not in items:
                items[task] = 0
            items[task] += 1
        priority_queue = [(-prio, label) for label, prio in items.items()]
        heapq.heapify(priority_queue)
        total_time = 0
        while priority_queue:
            removed_tasks = []
            for t in range(n + 1):
                if priority_queue:
                    prio, label = heapq.heappop(priority_queue)
                    if prio < -1:
                        removed_tasks.append((prio + 1, label))
                    total_time += 1
                elif not removed_tasks:
                    return total_time
                else:
                    total_time += 1
                    
            for removed_task in removed_tasks:
                heapq.heappush(priority_queue, removed_task)
        return total_time




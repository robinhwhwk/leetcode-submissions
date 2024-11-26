class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        total_time = 0
        last_occurence = dict()
        for task in tasks:
            if task in last_occurence:
                min_time = max(total_time + 1, last_occurence[task] + space + 1)
                last_occurence[task] = min_time
                total_time = min_time
            else:
                total_time += 1
                last_occurence[task] = total_time
        return total_time
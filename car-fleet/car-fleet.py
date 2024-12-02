class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [[position[i], (target-position[i])/speed[i]] for i in range(len(position))]
        times.sort() # sorted by position from smallest
        res = 1
        slowest_time = times[-1][1]
        for i in range(len(times) - 2, -1, -1):
            if times[i][1] > slowest_time:
                slowest_time = times[i][1]
                res += 1
        return res

       

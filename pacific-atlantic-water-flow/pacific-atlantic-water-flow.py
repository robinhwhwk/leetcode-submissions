class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_queue = []
        atlantic_queue = []
        pacific_visited = set()
        atlantic_visited = set()
        res = set()
        # add to pacific along i = 0 or j = 0
        # add to atlantic along i = len(heights) - 1, j = len(heights[0]) - 1
        for i in range(len(heights)):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, len(heights[0])-1))
        for j in range(len(heights[0])):
            pacific_queue.append((0, j))
            atlantic_queue.append((len(heights)-1, j))
        # process pacific queue
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while pacific_queue:
            size = len(pacific_queue)
            for i in range(size):
                row, col = pacific_queue.pop(0)
                pacific_visited.add((row, col))
                for d in directions:
                    nr, nc = row + d[0], col + d[1]
                    if nr < 0 or nr >= len(heights) or nc < 0 or nc >= len(heights[0]) or (nr, nc) in pacific_visited or heights[nr][nc] < heights[row][col]:
                        continue
                    pacific_queue.append((row + d[0], col + d[1]))
        while atlantic_queue:
            size = len(atlantic_queue)
            for i in range(size):
                row, col = atlantic_queue.pop(0)
                atlantic_visited.add((row, col))
                if (row, col) in pacific_visited:
                    res.add((row, col))
                for d in directions:
                    nr, nc = row + d[0], col + d[1]
                    if nr < 0 or nr >= len(heights) or nc < 0 or nc >= len(heights[0]) or (nr, nc) in atlantic_visited or heights[nr][nc] < heights[row][col]:
                        continue
                    atlantic_queue.append((row + d[0], col + d[1]))
        return list(res)
        


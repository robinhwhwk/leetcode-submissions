class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
        time = 0
        dirs = [1, 0, -1, 0, 1]
        while queue:
            size = len(queue)
            for i in range(size):
                row, col = queue.pop(0)
                for j in range(4):
                    nr, nc = row + dirs[j], col + dirs[j + 1]
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] != 1:
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = "#"
            if queue:
                time += 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
        return time
            
            

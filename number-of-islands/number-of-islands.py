class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != "1":
                return
            grid[row][col] = "#"
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                dfs(i, j)
        return res
        
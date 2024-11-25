class Solution:
    def trap(self, height: List[int]) -> int:
        # process each cell one by one
        # compute maximum left and maximum right
        # the value added for each cell is min(maxLeft, maxRight) - height
        maxLeft = [0 for _ in range(len(height) + 1)]
        maxRight = [0 for _ in range(len(height) + 1)]
        res = 0
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])
        for j in range(len(height) - 2, -1, -1):
            maxRight[j] = max(maxRight[j + 1], height[j + 1])
            minLeftRight = min(maxLeft[j], maxRight[j])
            if minLeftRight > height[j]:
                res += minLeftRight - height[j]
        return res

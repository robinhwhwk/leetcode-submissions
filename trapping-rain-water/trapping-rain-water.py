class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0 for _ in range(len(height))]
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i - 1])
        max_right = [0 for _ in range(len(height))]
        for j in range(len(height) - 2, -1, -1):
            max_right[j] = max(max_right[j + 1], height[j + 1])
        # now we have 2 arrays, max_left and max_right that contains max height for left and right for each index
        total = 0
        for k in range(len(height)):
            min_left_right = min(max_left[k], max_right[k])
            if height[k] < min_left_right:
                total += min_left_right - height[k]
            print("index", k)
            print(total)
        return total
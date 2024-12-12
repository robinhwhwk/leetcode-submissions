class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        total = 0
        max_left = max_right = 0
        while left <= right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            minLR = min(max_left, max_right)
            if height[left] < height[right]:
                if minLR > height[left]:
                    total += minLR - height[left]
                left += 1
            else:
                if minLR > height[right]:
                    total += minLR - height[right]
                right -= 1
        return total
            
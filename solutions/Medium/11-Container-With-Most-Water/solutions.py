class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        left = 0
        right = len(height) - 1
        while left < right:
            newmax = min(height[left],height[right])*(right - left)
            maximum = maximum if maximum > newmax else newmax
            if height[left] > height[right]:
                right-= 1
            elif height[left] <= height[right]:
                left +=1
        return maximum
        
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxArea = 0

        while (left < right):
            if height[left] < height[right]:
                maxArea = max(maxArea, height[left] * (right - left))
                left += 1
            else:
                maxArea = max(maxArea, height[right] * (right - left))
                right -= 1

        return maxArea
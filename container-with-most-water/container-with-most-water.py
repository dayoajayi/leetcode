class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        running_max_area = 0

        while l != r:
            area = min(height[l], height[r]) * (r - l)
            
            if area > running_max_area:
                running_max_area = area
                
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return running_max_area
                
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) -1
        area = 0

        # we want to maximize the distance along the x axis and find the minimum height 

        while left < right:
            area = max(area, (right - left)*(min(height[left], height[right])))

            if height[left] < height[right]:
                left = left+1
            else:
                right = right-1 
        return area

s = Solution()
height = [1,8,6,2,5,4,8,3,7]

print(s.maxArea(height))
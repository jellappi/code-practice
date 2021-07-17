# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        
        water = 0
        
        for i in range(len(height) - 1):
            
            if height[left] <= height[right]:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                
        return water

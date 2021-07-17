# https://leetcode.com/problems/3sum/

class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output = []
        
        if len(nums) <= 2:
            return output
        
        if nums[0] == nums[-1] == 0:
            return [[0,0,0]]
        
        for i, num in enumerate(nums):
            
            if num > 0:
                return output
            
            if i > 0 and num == nums[i-1]:
                continue
            
            left_i, right_i = i+1, len(nums) - 1
            
            while left_i < right_i:
                
                sum_result = num + nums[left_i] + nums[right_i]
                
                if sum_result == 0:
                    output.append([num, nums[left_i], nums[right_i]])
                    
                    while left_i < right_i and nums[left_i] == nums[left_i + 1]:
                        left_i += 1
                        
                    while left_i < right_i and nums[right_i] == nums[right_i - 1]:
                        right_i -= 1
                        
                    left_i += 1
                    right_i -= 1
                    
                elif sum_result > 0:
                    right_i -= 1
                    
                else:
                    left_i += 1
                    
        return output

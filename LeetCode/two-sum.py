# https://leetcode.com/problems/two-sum/

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        
        for i, num in enumerate(nums):
            dic[num] = i
            
        for i, num in enumerate(nums):
            
            pair = target - num
            
            if pair in dic and dic[pair] != i:
                return [i, dic[pair]]

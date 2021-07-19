# https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        #nums.sort()
        #return sum([num for i, num in enumerate(nums) if i%2 == 0])
        
        return sum(sorted(nums)[::2])

# https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        start_idx = 0
        cur_gas = 0
        
        for i in range(len(gas)):
            
            if cur_gas + gas[i] - cost[i] < 0:
                start_idx = i+1
                cur_gas = 0
                
            else:
                cur_gas += gas[i] - cost[i]
                
        return start_idx

# https://leetcode.com/problems/daily-temperatures/

# Stack 풀이
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        days = [0] * len(temperatures)
        stack = []
        
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                days[last] = i - last
            stack.append(i)
            
        return days

# 시간초과 답안
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        if not temperatures:
            return []
        
        days = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            
            day = 1
            
            for j in range(i+1, len(temperatures)):
                if t < temperatures[j]:
                    days[i] = day
                    #done = True
                    break
                else:
                    day += 1
                
        return days

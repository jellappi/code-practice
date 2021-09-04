# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        
        if x == 0:
            return 0
        
        x_str = str(x).rstrip('0')
        if x_str[0] == '-':
            x_rev =  '-' + x_str[1:][::-1]
        else:
            x_rev = x_str[::-1]
            
        if (int(x_rev) >= 2 ** 31) or (int(x_rev) <= - 2 ** 31):
            return 0
        else:
            return int(x_rev)

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        
        for i, c in enumerate(s):
            dic = defaultdict(int)
            dic[c] += 1
            len_i = 1
            
            for j in range(i+1, len(s)):
                if s[j] not in dic.keys():
                    dic[s[j]] += 1
                    len_i += 1
                else:
                    break
                    
            max_len = max(max_len, len_i)
                    
        return max_len

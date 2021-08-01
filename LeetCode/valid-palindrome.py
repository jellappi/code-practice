https://leetcode.com/problems/valid-palindrome

#solution 1 (40ms)
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        
        if s == s[::-1]:
            return True
        else:
            return False

#solution 2 (52ms)
class Solution:
    def isPalindrome(self, s: str) -> bool:

        chrs = []

        for c in s:
            if c.isalnum():
                chrs.append(c.lower())

        for i in range(len(chrs)//2):
            if chrs[i] == chrs[-(i+1)]:
                #print(chrs[i], chrs[-(i+1)], 'O')
                pass
            else:
                #print(chrs[i], chrs[-(i+1)], 'X')
                return False

        return True

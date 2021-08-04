# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        def dfs(index, path):
            if len(path) == len(digits):
                comb.append(path)
                return
            
            for i in range(index, len(digits)):
                for c in dic[digits[i]]:
                    dfs(i+1, path+c)

        comb = []
        
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        dfs(0, '')
        
        return comb

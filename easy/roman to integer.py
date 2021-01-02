"""
  Source: https://leetcode.com/problems/roman-to-integer/discuss/947008/Python-O(n)-solution-with-92-Faster-(Easy-to-understand)-%3A) 
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        value = dict[s[len(s)-1]]
        idx = len(s) - 1
        
        while idx >= 1:
            curr = dict[s[idx]]
            prev = dict[s[idx-1]]
            
            if prev < curr:
                value -= prev
            else:
                value += prev
                
            idx -= 1 

        return value
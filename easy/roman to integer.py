# My solution that I attempted
class Solution:
  def romanToInt(self, s: str) -> int:
      
      dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
      value = 0
      
      usedSubtraction = False
      for i in range(len(s)):
          for j in range(1, len(s)):
              if usedSubtraction:
                  break
              else:
                  usedSubtraction = True
                  if s[i] == "I" and s[j] == "V": 
                      value += 4
                      break
                  elif s[i] == "I" and s[j] == "X":
                      value += 9
                      break
                  elif s[i] == "X" and s[j] == "L":
                      value += 40
                      break
                  elif s[i] == "X" and s[j] == "C":
                      value += 90
                      break
                  elif s[i] == "C" and s[j] == "D":
                      value += 400
                      break
                  elif s[i] == "C" and s[j] == "M":
                      value += 900
                      break
                  else:
                      value += dict[s[i]]
                      usedSubtraction = False
                      break
      
      return value


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
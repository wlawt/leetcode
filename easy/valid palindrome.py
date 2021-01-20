class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        out = []
        
        for char in s:
            if char.isalnum():
                out.append(char)
        
        return out == out[::-1]
        
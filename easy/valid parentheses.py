class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        
        stack = []
        
        pairs = {"(": ")", "{": "}", "[": "]"}
        
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    last = stack.pop()
                    if pairs[last] != char:
                        return False
        
        if stack:
            return False
        else:
            return True
            
        
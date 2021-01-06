class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip() # remove trailing 
        strs = s.split(" ")
        
        return len(strs[-1])
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # any negative number is false
        # make rev, check rev == x
        # also check if rev in constraints
        
        if x < 0:
            return False
        
        original = x
        rev = 0
        while x != 0:
            pop = x % 10
            x //= 10
            
            rev = rev * 10 + pop
        
        if -2**31 <= rev <= 2**31-1:
            if rev == original: 
                return True
        
        return False
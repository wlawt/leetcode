class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:  
        if digits[0] == 0:
            digits[-1] += 1
            return digits
        
        numStr = ""
        for num in digits:
            numStr += str(num)
        
        newNum = str(int(numStr) + 1)
        
        new_digits = []
        for num in newNum:
            new_digits.append(num)
            
        return new_digits
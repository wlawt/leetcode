class Solution:
    def reverse(self, x: int) -> int:
        isNeg = False
        if x < 0:
            isNeg = True
            x *= -1

        rev = 0
        while x != 0:
            pop = x % 10
            x //= 10

            rev = rev * 10 + pop

        if isNeg:
            rev *= -1

        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        else:
            return rev
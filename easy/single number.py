class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = []
        
        for num in nums:
            if num not in seen:
                seen.append(num)
            else:
                seen.remove(num)
        
        return seen[0]
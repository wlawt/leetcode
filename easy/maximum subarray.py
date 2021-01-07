class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float("-inf")
        currsum = 0
        
        for num in nums:
            if num + currsum > num:
                currsum += num
            else:
                currsum = num
            
            if currsum > maxsum:
                maxsum = currsum
            
        return maxsum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}
        res = []
        
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in idxs:
                res.append(idxs[diff])
                res.append(i)
            else:
                idxs[nums[i]] = i
        
        return res
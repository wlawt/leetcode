class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # num, index
        dict = {}
        
        out = []
        
        for i in range(len(numbers)):
            diff = target - numbers[i]
            
            if diff in dict:
                # not zero-based
                out.append(i+1)
                out.append(dict[diff]+1)
            else:
                dict[numbers[i]] = i
        
        out.sort()
        
        return out
        
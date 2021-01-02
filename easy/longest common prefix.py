# My solution: 74 / 123 cases passed
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        common = strs[0]
        
        for i in range(1, len(strs)):
            tmp = ""
            for s in strs[i]:
                if s in common:
                    tmp += s
                else:
                    break
            common = tmp
        
        if common == strs[0] and len(strs) > 1:
            return ""
        else:
            return common
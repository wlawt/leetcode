# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Passed 64/114 test cases
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
    
        self.l = 0
        self.r = 0
        self.sums = []
        
        def bfs(root):
            if root.left:
                self.l += root.left.val
                self.sums.append(self.l)
                bfs(root.left)
            
            if root.right:
                self.r += root.right.val
                self.sums.append(self.r)
                bfs(root.right)
            
            return targetSum in self.sums
    
        return bfs(root)
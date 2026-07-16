# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxpath = -float('inf')
        def dfs(node):
            if not node:
                return 0
            val = node.val
            if val > self.maxpath:
                self.maxpath = val
            left, right = dfs(node.left), dfs(node.right)
            lar = max(left, right)
            smal = min(left, right)
            if lar > 0 and (node.val + lar) > 0:
                val = node.val + lar
                if smal > 0 and (val + smal) > self.maxpath:
                    self.maxpath = val + smal
                if val > self.maxpath:
                    self.maxpath = val
            elif (node.val + lar) > 0:
                val = node.val
                if val > self.maxpath:
                    self.maxpath = val
            return val
        dfs(root)
        return self.maxpath
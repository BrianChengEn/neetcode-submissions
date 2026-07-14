# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, large):
            if not root:
                return 0
            
            good = 1 if root.val >= large else 0
            large = max(large, root.val)
            left, right = dfs(root.left, large), dfs(root.right, large)
            return good + left + right

        return dfs(root, root.val)       
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
            good = 0
            if root.val >= large:
                large = root.val
                good = 1
            left, right = dfs(root.left, large), dfs(root.right, large)
            return good + left + right
        res = dfs(root, root.val)
        return res           
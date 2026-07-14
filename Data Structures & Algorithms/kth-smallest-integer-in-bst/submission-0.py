# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        def inorder(root):
            if not root:
                return None
            nonlocal n, k
            left = inorder(root.left)
            if not left:
                n += 1
                if n == k:
                    return root.val
            right = inorder(root.right)
            return left or right
        return inorder(root)
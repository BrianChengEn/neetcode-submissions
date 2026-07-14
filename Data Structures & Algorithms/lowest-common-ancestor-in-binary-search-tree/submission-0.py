# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        node1 = self.lowestCommonAncestor(root.left, p , q)
        node2 = self.lowestCommonAncestor(root.right, p , q)
        if root.val == p.val or root.val == q.val:
            return root
        if node1 and node2 and node1.val == p.val and node2.val == q.val:
            return root
        if node1 and node2 and node2.val == p.val and node1.val == q.val:
            return root
        root = node1 if node1 else node2
        return root
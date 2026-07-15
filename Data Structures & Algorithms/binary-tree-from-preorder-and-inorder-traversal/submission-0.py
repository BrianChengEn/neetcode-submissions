# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {
            value : index for index, value in enumerate(inorder)
        }
        self.preorder_index = 0

        def dfs(left, right):
            if left > right:
                return None
            value = preorder[self.preorder_index]
            self.preorder_index += 1
            root = TreeNode(value)
            mid = inorder_index[value]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root
        return dfs(0, len(preorder) - 1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        que = deque()
        if root:
            que.append(root)
        level = 0

        while que:
            for i in range(len(que)):
                node = que.popleft()
                if node.right:
                    que.append(node.right)
                if node.left:
                    que.append(node.left)
            level += 1
        
        return level

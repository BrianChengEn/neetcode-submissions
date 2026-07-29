"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        oldToNew = {}

        def dfs(oldNode):
            if oldNode in oldToNew:
                return oldToNew[oldNode]
            
            newNode = Node(oldNode.val)
            oldToNew[oldNode] = newNode

            for n in oldNode.neighbors:
                newN = dfs(n)
                newNode.neighbors.append(newN)
            
            return newNode
        
        return dfs(node)
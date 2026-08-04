class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        visit = set()
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                    
                if not dfs(neighbor, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visit) == n
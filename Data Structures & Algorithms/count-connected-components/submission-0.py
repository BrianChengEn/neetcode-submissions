class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
                dfs(neighbor, node)
            
            return True
        
        res = 0

        for i in range(n):
            if dfs(i, -1):
                res += 1
        
        return res
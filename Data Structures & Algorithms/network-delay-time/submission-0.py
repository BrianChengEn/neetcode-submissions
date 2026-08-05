class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for source, target, time in times:
            graph[source].append([target, time])
        
        res = 0
        minHeap = [[0, k]]
        visit = set()

        while minHeap:
            cur_time, vertex = heapq.heappop(minHeap)

            if vertex in visit:
                continue
            
            visit.add(vertex)
            res = cur_time

            for neighbor, travel_time in graph[vertex]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [cur_time + travel_time, neighbor])
        
        if len(visit) != n:
            return -1
        
        return res
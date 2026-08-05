class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for source, destination in tickets:
            heapq.heappush(graph[source], destination)
        
        route = []

        def dfs(airport):

            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)
            
            route.append(airport)
        
        dfs("JFK")

        return route[::-1]
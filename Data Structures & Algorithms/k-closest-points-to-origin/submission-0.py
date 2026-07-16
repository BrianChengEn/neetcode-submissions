class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [[x**2 + y**2, x, y] for x, y in points]
        heapq.heapify(dist)
        res = []
        for _ in range(k):
            x, y = heapq.heappop(dist)[1:3]
            res.append([x, y])
        return res
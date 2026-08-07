class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]

        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while minHeap:
            elevation, row, col = heapq.heappop(minHeap)

            if (row, col) in visit:
                continue
            
            visit.add((row, col))

            if row == len(grid) - 1 and col == len(grid) - 1:
                return elevation

            for dr, dc in direction:
                nr, nc = row + dr, col + dc
                if (
                    0 <= nr < len(grid) and
                    0 <= nc < len(grid) and
                    (nr, nc) not in visit
                ):
                    new_elevation = max(elevation, grid[nr][nc])
                    heapq.heappush(minHeap, [new_elevation, nr, nc])
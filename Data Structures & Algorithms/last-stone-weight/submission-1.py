class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-s for s in stones]
        heapq.heapify(s)
        while len(s) > 1:
            first = heapq.heappop(s)
            second = heapq.heappop(s)
            if second > first:
                heapq.heappush(s, first - second)
        if not s:
            s.append(0)
        return -s[0]
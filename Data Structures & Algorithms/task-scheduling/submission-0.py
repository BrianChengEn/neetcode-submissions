class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-val for val in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
            
            cnt = heapq.heappop(maxHeap) + 1
            if cnt != 0:
                q.append([cnt, time + n + 1])
        return time
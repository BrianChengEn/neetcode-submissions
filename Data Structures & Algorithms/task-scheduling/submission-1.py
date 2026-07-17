class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxFre = max(count.values())

        sameFre = 0
        for fre in count.values():
            if fre == maxFre:
                sameFre += 1
        
        res = (maxFre - 1) * (n + 1) + sameFre
        return max(res, len(tasks))
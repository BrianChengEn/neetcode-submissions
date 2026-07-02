class TimeMap:

    def __init__(self):
        self.tmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmap:
            self.tmap[key] = []
        self.tmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmap or self.tmap[key][0][1] > timestamp:
            return ""
        l = 0
        r = len(self.tmap[key]) - 1
        while l < r:
            m = (l + r + 1) // 2
            if self.tmap[key][m][1] <= timestamp:
                l = m
            else:
                r = m - 1
        return self.tmap[key][l][0]
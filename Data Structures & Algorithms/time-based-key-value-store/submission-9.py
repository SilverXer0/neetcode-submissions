from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list) # key -> [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        li = self.d[key]
        l = 0
        r = len(li) - 1
        res = (0, "")
        while l <= r:
            m = (l + r) // 2
            if li[m][0] > timestamp:
                r = m - 1
            elif li[m][0] < timestamp:
                if res[0] <= li[m][0]:
                    res = li[m]
                l = m + 1
            else:
                return li[m][1]

        return res[1]
            
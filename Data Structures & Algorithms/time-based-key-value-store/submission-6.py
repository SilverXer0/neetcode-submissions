class TimeMap:

    def __init__(self):
        self.store = {} #(key: [(value, timestamp)])

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        res = ""
        li = self.store[key]
        l = 0
        r = len(li) - 1

        while l <= r:
            m = (l + r) // 2
            if li[m][1] <= timestamp:
                res = li[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
        
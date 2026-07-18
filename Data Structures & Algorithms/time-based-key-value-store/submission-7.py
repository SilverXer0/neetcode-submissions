class TimeMap:

    def __init__(self):
        self.store = {} #(key: [(value, timestamp)])

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))            

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        li = self.store.get(key, [])

        left = 0
        right = len(li) - 1
        while left <= right:
            mid = (left + right) // 2
            if li[mid][1] <= timestamp:
                res = li[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res
        
        
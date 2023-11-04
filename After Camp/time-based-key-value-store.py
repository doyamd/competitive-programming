class TimeMap:

    def __init__(self):
        self.arr = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.arr[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        index = bisect.bisect(self.arr[key],[timestamp+1])-1
        if index == -1:
            return ''
        return self.arr[key][index][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
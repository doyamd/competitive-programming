class MyHashMap:

    def __init__(self):
        self.d = {}

    def put(self, key: int, value: int) -> None:
        self.d[key] = value

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        else:
            return self.d[key]

    def remove(self, key: int) -> None:
        self.d[key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
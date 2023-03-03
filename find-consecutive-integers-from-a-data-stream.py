class DataStream:

    def __init__(self, value: int, k: int):
        self.lis = []
        self.val = value
        self.size = k
        self.i = 0
        self.j = -1
        self.d = defaultdict(int)
    def consec(self, num: int) -> bool:
        self.lis.append(num)
        self.j += 1
        self.d[num] += 1
        if self.j - self.i +1 > self.size:
            self.d[self.lis[self.i]] -= 1
            self.i += 1
        if self.d[self.val] == self.size :
            return True
        else:
            return False
        
            


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
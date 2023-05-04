class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.large = nlargest(self.k,nums)
       
        heapify(self.large)
        

    def add(self, val: int) -> int:
        heappush(self.large,val)
        while len(self.large) > self.k:
            heappop(self.large)
        return self.large[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
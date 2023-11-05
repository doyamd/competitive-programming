class NumArray:

    def __init__(self, nums: List[int]):
        self.pre = []
        self.pre.append(0)
        for i in range(len(nums)):
            self.pre.append(self.pre[-1]+nums[i])
    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right+1] - self.pre[left]
        

#0 -2  -2  1  -4  -2 -3
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

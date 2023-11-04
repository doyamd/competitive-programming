class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [0 for _ in range(length)]
        self.org = [[[-1,0]] for _ in range(length)]
        self.id = 0 
    def set(self, index: int, val: int) -> None:
        self.org[index].append([self.id,val])
        

    def snap(self) -> int:
        self.id += 1
        return self.id-1

    def get(self, index: int, snap_id: int) -> int:
        indx = bisect.bisect(self.org[index],[snap_id+1])-1
        return self.org[index][indx][1]  


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
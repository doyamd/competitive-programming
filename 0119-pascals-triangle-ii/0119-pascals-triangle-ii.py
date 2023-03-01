class Solution:
    def getRow(self, row: int) -> List[int]:
        if row == 0 or row == 1:
            return [1]*(row+1)
        
        ans = [1]
        lis = self.getRow(row-1)
        for i in range(len(lis)-1):
            ans.append(lis[i]+ lis[i+1])
        ans.append(1)
        return ans
        
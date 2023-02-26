class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        
        for i in range(len( self.pre)):
            for j in range(len(self.pre[0])):
                if i == 0 and j == 0:
                    self.pre[i][j] = matrix[i][j]
                elif i == 0  and j > 0:
                    self.pre[i][j] = self.pre[i][j-1] + matrix[i][j]
                elif j == 0 and i > 0:
                    self.pre[i][j] = self.pre[i -1][j] + matrix[i][j]
                else:
                    self.pre[i][j] = self.pre[i-1][j] + self.pre[i][j-1] - self.pre[i-1][j-1] + matrix[i][j]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        upper = 0
        left = 0
        corner = 0
        if row1-1 >= 0:
            upper = self.pre[row1-1][col2]
        if col1-1 >= 0:
            left = self.pre[row2][col1-1]
        if row1-1 >= 0 and col1-1 >= 0:
            corner = self.pre[row1-1][col1-1]
       
        return self.pre[row2][col2] - upper - left + corner


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
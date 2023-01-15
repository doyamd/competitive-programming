class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        zeros = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    unique = i * col + j
                    zeros.add(unique)
        for i in range(row):
            for j in range(col):
                if i * col + j in zeros:
                    r=i
                    c=j
                    while r > 0 :
                        r -= 1
                        matrix[r][c]=0
                    r=i
                    while r < row-1:
                        r += 1
                        matrix[r][c]=0
                    r=i
                    while c > 0 :
                        c -= 1
                        matrix[r][c]=0
                    c=j
                    while c < col-1:
                        c += 1
                        matrix[r][c]=0
                    c=j
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
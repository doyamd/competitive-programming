class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        flag=True # checks if the diagonals are equal
        for row in range(len(matrix)-1):
            for col in range(len(matrix[0])-1):
                if matrix[row][col]==matrix[row+1][col+1]:
                    continue
                else: 
                    flag= False
                    break
        return flag
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag=False
        for i in range(len(matrix)):
            if matrix[i][0]==target:
                flag=True
            elif matrix[i][0]>target:
                for j in matrix[i-1]:
                    if target==j:
                        flag=True
            elif matrix[i][0]<target:
                for j in matrix[i]:
                    if target==j:
                        flag=True
        return flag
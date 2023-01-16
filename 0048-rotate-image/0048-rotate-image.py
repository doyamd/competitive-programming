class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length=len(matrix)
        temp=[0 for _ in range(length*length)]
        k=0
        for i in range(length):
            for j in range(length):
                temp[k]=matrix[i][j]
                k+=1
        k=0
        for j in range(length-1,-1,-1):
            for i in range(length):
                matrix[i][j]=temp[k]
                k+=1
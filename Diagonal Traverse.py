#
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        col_len=len(mat[0])
        row_len=len(mat)
        up=True
        col=0
        row=0
        diagonal=[]
        while col<col_len and row<row_len:
            if up:
                while col<col_len-1 and row>0:
                    diagonal.append(mat[row][col])
                    row-=1
                    col+=1
                diagonal.append(mat[row][col])
                if col==col_len-1:
                    row+=1
                else:
                    col+=1
            else:
                while col>0 and row<row_len-1:
                    diagonal.append(mat[row][col])
                    row+=1
                    col-=1
                diagonal.append(mat[row][col])
                if row==row_len-1:
                    col+=1
                else:
                    row+=1
            up=not(up)# changing direction
        return diagonal

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sums = 0
        i,j = 0,0
        while i < len(mat) and j < len(mat):
            sums += mat[i][j]
            i += 1
            j += 1
        i,j = 0, len(mat)-1
        while i < len(mat) and j > -1:
            if i != j:
                sums += mat[i][j]
            j -= 1
            i += 1
        return sums

        
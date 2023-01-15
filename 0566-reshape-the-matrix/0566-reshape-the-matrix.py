class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = 0
        col = 0
        if len(mat) * len(mat[0]) != r*c:
            return mat
        
        res = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if col<c:
                    res[row][col] = mat[i][j]
                    col += 1
                else:
                    row += 1
                    col = 0
                    res[row][col] = mat[i][j]
                    col+=1
        return res
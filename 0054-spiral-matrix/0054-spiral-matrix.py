class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        col = len(matrix[0])
        row = len(matrix)
        lis = []
        top_l = 0
        top_r = col-1
        bott_l = 0
        bott_r = row - 1

        while len(lis)< row * col:
            i = bott_l

            while i <= top_r and len(lis) < row * col:
                lis.append(matrix[top_l][i])
                i += 1
            i = top_l + 1
            top_l += 1
            
            while i <= bott_r and len(lis) < row * col:
                lis.append(matrix[i][top_r])
                i += 1
            i = top_r - 1
            top_r -= 1

            while i >= bott_l and len(lis) < row * col:
                lis.append(matrix[bott_r][i])
                i -= 1
            i=bott_r - 1
            bott_r -= 1

            while i >= top_l and len(lis) < row * col:
                lis.append(matrix[i][bott_l])
                i -= 1
            bott_l += 1

            if top_r == top_l == bott_r == bott_l:
                lis.append(matrix[top_l][bott_r])


        return lis
        
        
        
        
        
        
        
        
        
        
        
        
        
        
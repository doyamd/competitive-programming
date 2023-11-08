class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d ={}
        
        for i in range(9):
            for num in range(1,10):
                d[num] = 0
            for j in range(9):
                if board[i][j] != ".":
                    d[int(board[i][j])] += 1 
            for valid in d.values():
                if valid > 1:
                    return False
        for i in range(9):
            for num in range(1,10):
                d[num] = 0
            for j in range(9):
                if board[j][i] != ".":
                    d[int(board[j][i])] += 1 
            for valid in d.values():
                
                if valid > 1:
                    return False
    
        for row in range(0,9,3):
            for col in range(0,9,3):
                for num in range(1,10):
                    d[num] = 0
                for i in range(row, row+3):
                    for j in range(col,col+3):
                        if board[i][j] != ".":
                            d[int(board[i][j])] +=1
                for valid in d.values():
                    if valid > 1:
                        return False
        
        return True
            
            
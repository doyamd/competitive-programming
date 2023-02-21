class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        d = {}
        
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                sums = 0
                for k in range(i,i+3):
                        sums += grid[k][j]
                for x in range(1,10):
                        d[x] = 0
                #print(sums)
                ans = True
                #row check
                for r in range(i,i+3):
                    total = 0
                    for c in range(j, j+3):
                        if grid[r][c] < 10 and grid[r][c] >0:
                            d[grid[r][c]] += 1
                            if d[grid[r][c]] > 1:
                                ans = False
                                #continue
                        else: 
                            ans = False
                            #continue
                        total += grid[r][c]
                    if total != sums:
                        ans = False
                        #continue
                    
                #col check
                for c in range(j, j+3):
                    total = 0
                    for r in range(i,i+3):
                        total += grid[r][c]
                    if total != sums:
                        ans = False
                        #continue
                    #print (ans)
                row = i
                col = j
                diag_r = 0
                diag_l = 0
                while row < i + 3 and col < j + 3:# sum of the diagonal right
                    diag_r += grid[row][col]
                    row += 1
                    col += 1
                if diag_r != total:
                    ans = False
                col = j + 2
                row = i
                while row < i+3 and col >= 0:# sum of the diagonal left
                    diag_l += grid[row][col]
                    row += 1
                    col -= 1
                if diag_l != total:
                    ans = False
                #check all the sums are equal
                if ans:
                    count += 1
                    
        return count
                
       
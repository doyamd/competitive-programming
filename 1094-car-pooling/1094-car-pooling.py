class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxi = 0
        ans = True
        sums = 0
        path = []
        for i in range(len(trips)):
            for j in range(3):
                maxi = max(maxi,trips[i][j])
        
        for i in range(maxi+1):
            path.append(0)
        
        for i in range(len(trips)):
            for j in range(1,3):
                if j == 1:
                    path[trips[i][j]] += trips[i][0]
                if j == 2:
                    path[trips[i][j]] += -1*trips[i][0]
                
        for i in path:
            sums += i
            if sums > capacity:
                ans = False
        return ans
            
                
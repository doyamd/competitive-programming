#https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/description/
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_indx=-1
        min_dis=10000 #maximum distance constraint
        for i in range(len(points)):
            indx_dis=[]
            if points[i][0]==x or points[i][1]==y:
                dis=abs(x-points[i][0])+abs(y-points[i][1])
                if dis<min_dis:
                    min_dis=dis
                    min_indx=i
               
        return min_indx
        
                
      
        
        

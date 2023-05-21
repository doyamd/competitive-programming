class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d = list(range(len(points)))
        
        def find(i):
            if i != d[i]:
                d[i] = find(d[i])
            return d[i]

        def union(x,y):
            repx = find(x)
            repy = find(y)

            if repx != repy:
                d[repy] = repx
                return True
            return False
        conect = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                conect.append((dis,i,j))
        ans = 0
        count = 0
        conect.sort()
        for dis, i, j in conect:
            if union(i,j):
                ans += dis
                count += 1
        return ans
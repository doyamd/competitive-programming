from typing import List
from collections import defaultdict, deque

from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        ans = [0 for _ in range(n)]
        d = defaultdict(list)
        length = defaultdict(int) 
        for x,y in edges:
            d[x].append(y)
            length[y] += 1
        queue = deque()
        for i in range(1,n+1):
            if length[i] == 0:
                queue.append(i)
        # print(queue)
        while queue:
            num = queue.popleft()
            ans[num-1] += 1
            for i in d[num]:
                ans[i-1] = max(ans[i-1],ans[num-1])
                length[i] -= 1
                if length[i] == 0:
                    queue.append(i)
                
        return ' '.join([str(v) for v in ans])
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        def backtrack(indx,arr):
            if len(arr) == k:
                path.append(arr)
                return 
            
            for i in range(indx+1,n+1):
                backtrack(i, arr + [i])



        for i in range(1,n+1):
            backtrack(i,[i])
        return path
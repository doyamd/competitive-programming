class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = [0 for _ in range(101)]
        
        for b, d in logs:
            arr[b-1950] += 1
            arr[d-1950] -= 1
        ans = [arr[0],1950]
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
            if arr[i] > ans[0]:
                ans[0] = arr[i]
                ans[1] = 1950+i
        return ans[1]
        

            


        
class Solution:
    def closestPrimes(self, left: int, n: int) -> List[int]:
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        arr = []
        
        for p in range(2, n+1):
            if prime[p] and p >= left:
                arr.append(p)

        mini = float('inf')
        ans = [-1,-1]
        for i in range(len(arr)-1):
            diff = abs(arr[i] - arr[i+1])
            if diff  < mini:
                mini = diff
                ans = [arr[i], arr[i+1]]
                
       
        return ans
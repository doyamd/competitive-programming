class Solution:
    def countOrders(self, n: int) -> int:
        dp  = [0]*n
        for i in range(n):
            x = i+1
            num = ((x*2) * ((x*2)-1))//2
            dp[i] = num
        # print(dp)
        return prod(dp) % ((10**9)+7)
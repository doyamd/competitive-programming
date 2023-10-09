class Solution:
    def knightDialer(self, n: int) -> int:
        d = {0:[4,6],1:[6,8],2:[7,9],3:[4,8],4:[0,3,9],6:[0,1,7],7:[2,6],8:[1,3],9:[2,4]}
        memo = defaultdict(int)
        count = 0
        if n == 1:
            return 10
        def dp(i,num):
            if num == 0:
                return 1
            if i == 5:
                return 0
            sums = 0
            for j in d[i]:
                if not memo[(j,num)]:
                    memo[(j,num)] = dp(j,num-1)
                sums += memo[(j,num)]
            return sums
            
        for i in range(10):
            count += dp(i,n-1)
        return (count%(10**(9) + 7))
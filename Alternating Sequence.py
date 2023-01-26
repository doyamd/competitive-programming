#https://codeforces.com/contest/1343/problem/C
    test =int(input())
    for i in range(test):
        size = int(input())
        lis =  list(map(int,input().split()))
        pos = True if lis[0]>0 else False
        maxi=lis[0]
        ans = 0
        for i in range(size):
            if pos != (lis[i]>0):
                pos = not pos
                ans += maxi
                maxi = lis[i]
            else:
                if lis[i]>maxi:
                    maxi = lis[i]
        ans +=maxi 
        print(ans)  

#https://codeforces.com/gym/436344/problem/A
test = int(input())
for t in range(test):
    size = int(input())
    lis = list(map(int,input().split()))
    ans = 0
    for i in range(size):
        xor = 0
        for j in range(size):
            if i != j:
                xor ^= lis[j]
        if lis[i] == xor:
            ans = lis[i]
            break
    
    print(ans)

n = int(input())
ans = 0
for i in range(n):
    arr = list(map(int,input().split()))
    ans += arr.count(1)
print(ans//2)
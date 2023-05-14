#https://codeforces.com/gym/439769/problem/A
size, des = map(int,input().split())
lis = list(map(int,input().split()))
i = 1
ans = ''
while i < des:
    i = i + lis[i-1]
    if i == des:
        ans = "YES"
        break

if not ans:
    ans ="NO"
print(ans) 

#https://codeforces.com/problemset/problem/90/B
row, col = map(int,input().split())
arr = []
ans = ''
for i in range(row):
    arr.append(list(input()))
for i in range(row):
    for j in range(col):
        cross = False
        for k in range(row):
            if arr[i][j] == arr[k][j] and i!=k:
                cross = True
        for k in range(col):
            if arr[i][j] == arr[i][k] and j!=k:
                cross = True
        if not cross:
            ans +=arr[i][j]
    

print(ans)

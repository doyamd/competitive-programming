#https://codeforces.com/problemset/problem/1399/A
tests = int(input())
for test in range(tests):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    i=1
    flag = True
    while i < n:
        if arr[i] - arr[i-1] > 1:
            flag = False
            break
        i+=1
    if flag:
        print("YES")
    else:
        print("NO")

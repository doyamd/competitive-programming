#https://codeforces.com/problemset/problem/977/C
size, num = map(int, input().split())
lis = list(map(int, input().split()))
lis.sort()
if num == 0 and lis[num]-1 >= 1:
    print(lis[num]-1)
elif num == size and lis[num-1] >= 1:
    print(lis[num-1])
elif lis[num-1] < lis[num]:
    print(lis[num-1])
elif lis[num-1] + 1 <= lis[num] and lis[num-1]+1 >= 1:
    print(lis[num-1]+1)
else:
    print(-1)

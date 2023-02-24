#https://codeforces.com/gym/426933/problem/A
num = int(input())
lis = list(map(int, input().split()))
sum1 = 0
sum2 = 0
for i in range(num):
    sum1 += lis[i]
for i in range(num,len(lis)):
    sum2 += lis[i]
i = 0
j = len(lis) - 1  
if sum1 == sum2 :
    lis.sort()
    sum1 = 0
    sum2 = 0
    for i in range(num):
        sum1 += lis[i]
    for i in range(num,len(lis)):
        sum2 += lis[i]
    
if sum1 == sum2:
    print(-1)
else:
    print(*lis)

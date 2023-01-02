#https://codeforces.com/gym/419351/problem/C
n = int(input())
lis = list(map(int, input().split()))
count = 0
mini = lis[0]
maxi = lis[0]

for i in range(1, len(lis)):
    if lis[i] < mini:
       mini=lis[i]
       count+=1
    if lis[i] > maxi:
       maxi=lis[i]
       count += 1

print(count)

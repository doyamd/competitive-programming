#https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A
num =list(map(int,input().split()))
n1= num[0]
n2= num[1]
lis1 = list(map(int,input().split()))
lis2 = list(map(int,input().split()))
i=0
j=0
ans=[]
while i< n1 and j < n2:
    if lis1[i] < lis2[j]:
        ans.append(lis1[i])
        i+=1
    else:
        ans.append(lis2[j])
        j+=1
 
if i <  n1:
    while i < n1:
        ans.append(lis1[i])
        i+=1
if j < n2:
    while j < n2:
        ans.append(lis2[j])
        j+=1
print(*ans

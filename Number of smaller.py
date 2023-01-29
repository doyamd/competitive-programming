#https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B
n, m =(map(int,input().split()))
lis1 = list(map(int,input().split()))
lis2 = list(map(int,input().split()))
ans = []
j=0 
for num in lis2:
    while j < len(lis1) and lis1[j] < num:
        j += 1
    ans.append(j)
        
print(*ans)

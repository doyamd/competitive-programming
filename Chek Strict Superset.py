A=set(map(int,input().split()))# the main set
n=int(input())
i=0
ans=True
while i<n:
    lis=set(map(int,input().split()))# the sub sets to be checked
    if A.issuperset(lis)==False:
        ans=False
    i+=1
print(ans)

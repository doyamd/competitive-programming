#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem/
from collections import defaultdict
nums=list(map(int,input().split()))
A=[]
B=[]
i=0
while i< nums[0]:
    A.append(input())
    i+=1
i=0
while i < nums[1]:
    B.append(input())
    i+=1
diction_A=defaultdict(list)
for indx in range(len(A)):
    diction_A[A[indx]].append(indx+1)

for wrd in B:
    ans=[]
    if diction_A[wrd]:
        ans=diction_A[wrd]
        print(*ans)
    else:
        print(-1)

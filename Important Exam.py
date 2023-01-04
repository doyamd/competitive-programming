#https://codeforces.com/gym/419829/problem/B
nums=list(map(int,input().split()))
studs=nums[0]
ques=nums[1]
i=0
A=['A','B','C','D','E']
d = {}

lis=[]
ans=[]

sum=0
while i<studs:
    lis.append(input())
    i+=1
score=list(map(int,input().split()))
i=0

while i<ques:
    for k, keys in enumerate(A):
        d[keys] = 0

    for j in range(studs):
         d[lis[j][i]]+=1
    multi=max(d.values())
   
    ans.append(score[i]*multi)
    i+=1
for i in ans:
    sum+=i
print(sum)


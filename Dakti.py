#https://codeforces.com/gym/419351/problem/B
n=int(input())
i=0
while i < n:
    sorting = []
    lis=list(input().split())
    for j in range(len(lis)):
        num = str([int(x) for x in lis[j] if x.isdigit()])
        word = lis[j].replace(num[1],'')
        sorting.append(str(num[1])+word)
    sorting.sort()
    for j in range(len(sorting)):
        sorting[j]=sorting[j].replace(sorting[j][0],'')
    ans=' '.join(sorting)
    print(ans)
    i += 1

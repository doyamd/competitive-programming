#https://codeforces.com/gym/425418/problem/A
test = int(input())
for indx in range(test):
    ans = []
    size = int(input())
    lis = list(map(int, input().split()))
    i = 0
    j = size -1
   
    while i<= j:
        if i == j:
            ans.append(lis[i])
        else:
            ans.append(lis[i])
            ans.append(lis[j])
        i += 1
        j -= 1

    print(*ans)

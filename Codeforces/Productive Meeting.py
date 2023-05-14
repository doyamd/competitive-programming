#https://codeforces.com/gym/442099/problem/C

import heapq
test = int(input())
for t in range(test):
    num = int(input())
    lis = list(map(int,input().split()))
    heap = []
    for i in range(num):
        lis[i] = -1*lis[i]
        if lis[i]:
            heapq.heappush(heap,(lis[i],i))

    ans = 0
    arr = []
    while len(heap) > 1:
        num1,ind1 = (heapq.heappop(heap))
        num2,ind2 = (heapq.heappop(heap))
        ans += 1
        arr.append([ind1+1,ind2+1])
        if num1 < -1:
            heapq.heappush(heap,(num1+1, ind1))
        if num2 < -1:
            heapq.heappush(heap,(num2+1,ind2))

    print(ans)

    for x,y in arr:
            print(x,y)

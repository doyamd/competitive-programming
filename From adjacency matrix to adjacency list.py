from collections import defaultdict
row = int(input())
d = defaultdict(list)
for r in range(1,row+1):
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        if arr[i] == 1:
            d[r].append(i+1)
for i in d:
    print(len(d[i]), *d[i])
    

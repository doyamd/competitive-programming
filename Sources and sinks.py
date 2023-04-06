from collections import defaultdict
row = int(input())
d = defaultdict(int)
source = []
sink = [] 
for r in range(1,row+1):
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        d[i+1] += arr[i]
    one = arr.count(1)
    if one == 0:
        sink.append(r)
for i in d:
    if d[i] == 0:
        source.append(i)
source.sort()
sink.sort()
print(len(source), *source)
print(len(sink), *sink)

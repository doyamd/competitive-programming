#https://codeforces.com/gym/440884/problem/B
from collections import defaultdict
from collections import deque
size = int(input())
count = 0
ans = 0
d = defaultdict(list)

for l in range(size):
    arr = input().split()
    arr[0] = arr[0].lower()
    arr[2] = arr[2].lower()
    d[arr[2]].append(arr[0])
queue = deque(['polycarp'])
visited = set()

while queue:
    count += 1
    for l in range(len(queue)):
        reposter = queue.popleft()
        if reposter not in visited:
            visited.add(reposter)
            for i in d[reposter]:
                queue.append(i)
    ans = max(ans,count)
    
print(ans)

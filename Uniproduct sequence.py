#https://codeforces.com/gym/425418/problem/B
size = int(input())
arr = list(map(int, input().split()))
count = 0
neg = 0
zer = 0
i = 0
while i < size:
    if arr[i] < 0:
        count += -1 - arr[i]
        neg += 1
    elif arr[i] == 0:
        zer += 1
        count += 1
        
    elif arr[i] > 0:
        count += arr[i] - 1
        
    i += 1
if neg % 2 != 0 and zer == 0:
    count += 2
print(count)

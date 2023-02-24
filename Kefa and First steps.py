#https://codeforces.com/gym/428166/problem/B
size = int(input())
arr =list(map(int,input().split()))
i = 0
j = 1
maxi =0
while j < size:
    if arr[j-1] <= arr[j]:
        j += 1
    else:
        maxi =max(maxi, j-i)
        
        i = j
        j += 1
maxi =max(maxi, j-i)
print(maxi)

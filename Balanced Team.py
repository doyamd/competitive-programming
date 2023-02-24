#https://codeforces.com/gym/428166/problem/D
size = int(input())
arr =list(map(int,input().split()))
i = 0
j = 1
maxi =0
arr.sort()
while j < size:
    if arr[j] - arr[i] <= 5:
        j += 1
    else:
        maxi =max(maxi, j-i)
        i += 1 
        
maxi =max(maxi, j-i)
print(maxi)

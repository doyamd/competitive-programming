#https://codeforces.com/gym/425418/problem/C
size = int(input())
lis = list(map(int, input().split()))
ans = []
count = 0

for i in range(size):
    mini = i
    for j in range (i+1, size):
        if lis [j] < lis[mini]:
            mini = j
    if i != mini:
        lis [i], lis[mini] = lis[mini], lis[i]
        count += 1
        ans.append(i)
        ans.append(mini)
print(count)
print(*ans)


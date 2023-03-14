size, ass = map(int,input().split())
days = [0 for i in range(size+1)]
ans = ""
for a in range(ass):
    start, end =  map(int,input().split())
    days[start] += 1
    days[end+1] += -1
for i in range(1,size):
    days[i] += days[i-1]
for i in days:
    if i == 0:
        ans = "YES"
        break
if ans == "":
    ans = "NO"
print(ans)

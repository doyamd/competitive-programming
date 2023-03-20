#https://codeforces.com/problemset/problem/1611/B
test = int(input())
for t in range(test):
    team = list(map(int, input().split()))
    ans = sum(team) // 4
    if team[1] < team[0] and team[1] < ans:
        ans = team[1]
    elif team[0] < team[1] and team[0] < ans:
        ans = team[0]
    print(ans)
        
        

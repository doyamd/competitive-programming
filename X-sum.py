#https://codeforces.com/contest/1676/problem/D
from collections import defaultdict
test=int(input())
for itter in range(test):
    row,col=map(int,input().split())
    board=[0 for _ in range(row)]
    for i in range(row):
        lis=list(map(int, input().split()))
        board[i]=lis
    
        right=defaultdict(int)
        left=defaultdict(int)
        attack=0
    for r in range(row):
        for c in range(col):
            right[r-c]+=board[r][c]  
            left[r+c]+=board[r][c]  
    for r in range(row):
        for c in range(col):
            attack=max(attack,right[r-c]+left[r+c]-board[r][c])
    print(attack)

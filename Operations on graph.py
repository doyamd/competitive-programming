from collections import defaultdict
ver = int(input())
operation = int(input())
d = defaultdict(list)
for o in range(operation):
    oper =list( map(int, input().split()))
    if oper[0] == 1:
        d[oper[1]].append(oper[2])
        d[oper[2]].append(oper[1])
    elif oper[0] == 2 and d[oper[1]] != 0:
        print(*d[oper[1]])



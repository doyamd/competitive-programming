#https://codeforces.com/problemset/problem/1741/A
test_case=int(input())
dict={'S':0,'M':1,'L':2}
for i in range(test_case):
    shirt=input().split()
    t1=shirt[0]
    t2=shirt[1]
    t1_len=len(t1)-1
    t2_len=len(t2)-1
    if dict[t1[t1_len]] < dict[t2[t2_len]]:
        print('<')
    elif dict[t1[t1_len]] > dict[t2[t2_len]]:
        print('>')
    elif dict[t1[t1_len]] == dict[t2[t2_len]]:
        x1=t1.count('X')
        x2=t2.count('X')
        if x1<x2:
            if t1[t1_len]=='S':
                print('>')
            else:
                print('<')
        elif x1>x2:
            if t1[t1_len]=='S':
                print('<')
            else:
                print('>')
        else :
            print('=')

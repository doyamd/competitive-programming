#https://codeforces.com/gym/421441/problem/A
test_case=int(input())
square='No'
for test in range(test_case):
    a1,b1,=map(int,input().split())
    a2, b2, = map(int, input().split())

    if ((a1==0 and b1==0) and a2==b2) or ((a2==0 and b2==0) and a1==b1):
        square='Yes'
    else:
        if a1>0 and a2>0 and a1>0 and b2>0:
            if a1==a2 and b1+b2==a1:
                square='Yes'
            elif a1==b2 and a2+b1==a1:
                square='Yes'
            elif b1==a2 and a1+b2==a2:
                square='Yes'
            elif b1==b2 and a1+a2==b2:
                square='Yes'
            else:
                square = 'No'

    print(square)

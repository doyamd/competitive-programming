#https://www.hackerrank.com/challenges/py-set-difference-operation/problem/
E=input()
eng=set(map(int,input().split()))
F=input()
fren=set(map(int,input().split()))
ans=eng-fren
print(len(ans))

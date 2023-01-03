#https://www.hackerrank.com/challenges/py-set-union/problem/
e=int(input())
eng=set(map(int,input().split()))
f=int(input())
fren=set(map(int,input().split()))
ans=eng|fren
print(len(ans))

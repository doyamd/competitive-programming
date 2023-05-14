#https://codeforces.com/gym/437178/problem/D
from math import sqrt
from math import gcd
num = int(input())
square = int(sqrt(num))
i = square
while i :
    num2 = num//i
    gd = gcd(i, num2)
    if gd == 1 and num % i ==0:
        print(i, num2)
        break
    i -= 1

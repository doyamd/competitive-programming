#https://www.hackerrank.com/challenges/py-the-captains-room/problem
from collections import Counter

K, elements = int(input()), list(map(int, input().split()))

for element, count in Counter(elements).items():
    if count != K:
        print(element)

#https://www.hackerrank.com/challenges/word-order/
from collections import Counter
num = int(input())
words = []
for x in range(num):
      words.append(input())
answer= Counter(words)
print(len(answer))
print(*answer.values())

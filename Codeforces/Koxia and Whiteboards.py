#https://codeforces.com/gym/442099/problem/A
for t in range(test):
n,m = input().split()
board = list(map(int,input().split()))
oper = list(map(int,input().split()))
heapq.heapify(board)
for i in oper:
    heapq.heappop(board)
    heapq.heappush(board,i)
sums = 0
while board:
    sums +=heapq.heappop(board)

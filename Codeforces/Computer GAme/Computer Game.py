#https://codeforces.com/gym/440884/problem/D
from collections import deque
test = int(input())
for t in range(test):
  col = int(input())
  grid = [[0 for _ in range(col)] for _ in range(2)]
  for r in range(2):
      path = input()
      for c in range(col):
          if path[c] == "1":
              grid[r][c] = 1
  direc = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
  def inbound(i,j):
      if i < 0 or i >= 2 or j < 0 or j >= col or grid[i][j]== 1:
          return False
      else:
          return True
  queue = deque([(0,0)])
  visited = set()
  ans = ""
  while queue:
      for l in range(len(queue)):
          i,j = queue.popleft()
          if (i,j) == (1,col-1):
              ans = "YES"
              break
          if (i,j) not in visited:
              visited.add((i,j))
              for x,y in direc:
                  if inbound(i+x,j+y):
                      queue.append((i+x,j+y))
  if not ans:
      ans = "NO"
  print(ans)

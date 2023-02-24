#https://codeforces.com/gym/428166/problem/A
test = int(input())
for x in range(test):
    r1 = list(map(int,input().split()))
    r2 = list(map(int,input().split()))
    
    i = 0
    ans = False
  
    if r1[0] < r1[1] and r2[0] < r2[1] and r1[0] < r2[0] and r1[1] < r2[1]:

           
            ans = True
    
    else:
        
        while i < 5:
            r1[0],r1[1] = r1[1], r1[0]
            r2[0], r2[1] = r2[1], r2[0]
            r1[0],r2[1] = r2[1], r1[0]
            
            if r1[0] < r1[1] and r2[0] < r2[1] :
                if r1[0] < r2[0] and r1[1] < r2[1]:
                    ans = True
                    break
            i += 1
        
    if ans:
        print("YES")
    else:
        print("NO")

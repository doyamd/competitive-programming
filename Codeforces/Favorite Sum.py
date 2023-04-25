  #https://codeforces.com/gym/439769/problem/B 
  test = int(input())
    for t in range(test):
        size, lim = map(int,input().split())
        lis = list(map(int,input().split()))
        sums = (lim*(lim+1))//2 
        
        for i in lis: 
            if i <= lim:
                sums -= (2*i)
            
     
        print(sums)

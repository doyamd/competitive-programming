  #https://codeforces.com/gym/437178/problem/C  
  num = int(input())
     
    arr = [1 for i in range( num+2)]
    i = 2
    while i < num:
        j = 2 * i
        while j <= num+1:
            arr[j] = 2
            j += i
        i += 1
    if num > 2:
        print("2")
    else:
        print("1")
    print(*arr[2:])

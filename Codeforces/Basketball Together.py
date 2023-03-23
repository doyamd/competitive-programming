#https://codeforces.com/gym/433454/problem/A
size, num = map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()
#50 60 70 80 90 100
count = 0
i = 0
j = size-1
while i <= j :
    if lis[j] > num:
        count += 1
        j -= 1
    elif lis[j] == 0:
        break
    else:
        play = int(num/lis[j]) + 1
        if play <= (j-i)+1 and lis[j] * play > num and i != j:
            count += 1
        i += (play-1)
        j -= 1
        #print(play)
print(count)

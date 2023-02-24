#https://codeforces.com/gym/424075/problem/A
size =int (input())
lis = list(map(int, input().split()))
w =0
h =0
i=0
k=0
j=size-1
while i <= j:
    if lis[i] >= lis[j]:
        if k%2 == 0 :
             w +=lis[i]
        else:
            h +=lis[i]
        i +=1
    else:
        if k%2 == 0 :
             w +=lis[j]
        else:
            h +=lis[j]
        j -= 1
    k+=1
print(w, h)

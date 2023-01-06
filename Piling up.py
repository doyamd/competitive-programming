#https://www.hackerrank.com/challenges/piling-up/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
j=0
test_cases=int(input())
while j<test_cases:
    arr_len=int(input())
    array=list(map(int,input().split()))#the given length of blocks
    left=0
    right=arr_len-1
    ans="Yes"
    i=0
    stack=[]# our vertically stacked cubes
    if array[left]>=array[right]:
            stack=array[left]
            i+=1
            left+=1
    elif array[right]>=array[left]:
            stack=array[right]
            i+=1
            right-=1
    while left<=right :
        if array[left]>=array[right] and stack>=array[left]:
            stack=array[left]
            i+=1
            left+=1
        elif array[right]>=array[left] and stack>=array[right]:
            stack=array[right]
            i+=1
            right-=1
        else:
            ans="No"
            break
    print(ans)
    j+=1

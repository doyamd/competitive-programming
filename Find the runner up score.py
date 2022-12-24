#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/
if __name__ == '__main__':
    n = int(input())
    arr = list( map(int, input().split()))
    
    arr.sort(reverse=True)
    
    
    for number in arr:
        if arr[0]!=number:
            print(number)
            break
        if __name__ == '__main__':
    n = int(input())
    arr = list( map(int, input().split()))
    
    arr.sort(reverse=True)
    
    
    for number in arr:
        if arr[0]!=number:
            print(number)
            break
        
